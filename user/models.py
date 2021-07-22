import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=25, unique=True)
    name = models.CharField(_('first name'), max_length=150, null=True)
    phone = models.CharField(max_length=20, default='', null=True)
    delivery = models.CharField(max_length=1000, blank=False, null=False)
    admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # REQUIRED_FIELDS = ["first_name", "last_name", "gender", "birthday", "is_host"]

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


    @property
    def is_superuser(self):
        return self.admin

    class Meta:
        db_table = "login"
