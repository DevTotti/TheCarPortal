from django.urls import path
from .views import UserRegistrationView, UserLoginView


urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
]