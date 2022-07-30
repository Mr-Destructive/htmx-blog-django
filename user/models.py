from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    REQUIRED_FIELDS = ["email"]
