from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    password = models.EmailField()
    is_verified = models.IntegerField()
