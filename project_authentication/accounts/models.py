from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=15, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)  # image will be stored in root folder inside profile_images folder
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'

    objects = CustomUserManager()


    def __str__(self):
        return self.phone_number

