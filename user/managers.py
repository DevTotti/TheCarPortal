from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password, some_data):

        if not email:
            raise ValueError('Email is required!')

        if not password:
            raise ValueError('Password is required!')

        user = self.model(
            email=self.normalize_email(email),
            name=some_data.get('name'),
            phone=some_data.get('phone'),
            delivery=some_data.get('delivery'),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password):

        some_data = {}

        if not password:
            raise TypeError('SuperUsers must have password!')

        user = self.create_user(email, password, some_data)
        user.admin = True
        user.is_staff = True
        user.save()

        return user