from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    DoesNotExist = None
    mobile = models.CharField(max_length=10)
    age = models.IntegerField()
