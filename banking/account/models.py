from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=200)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class BankDetail(models.Model):
    ifsc = models.CharField(max_length=255)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=255)
    address = models.CharField(max_length=1080)
    city = models.CharField(max_length=500)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
