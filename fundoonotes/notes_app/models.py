from users.models import User
from django.db import models


# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1200)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
