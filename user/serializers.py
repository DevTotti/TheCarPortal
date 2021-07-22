from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import User

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER



class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        required=True,
        label="Password",
        style={'input_type': 'password'}
    )

    password2 = serializers.CharField(
        required=True,
        label="Confirm Password",
        style={'input_type': 'password'}
    )


    class Meta:
        model = User
        fields = '__all__'


    def create(self, valid_data):
        password = valid_data['password']
        email = valid_data['email']
        user = User.objects.create_user(email=email, password=valid_data['password'], some_data=valid_data)

        return user


class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.CharField(
        max_length=255,
        required=True,
        label="Email"
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        label="Password",
        style={'input_type': 'password'}
    )

    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )

        try:

            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)

        except User.DoesNotExist:

            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )


        return {
            'email':user.email,
            'token': jwt_token
        }