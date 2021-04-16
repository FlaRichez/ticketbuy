from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    wallet = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)


class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    average_rate = models.FloatField(default=0)


