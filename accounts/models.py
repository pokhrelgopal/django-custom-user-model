from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    image = models.ImageField(upload_to="profile/", null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
