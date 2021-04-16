from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from ticketbuy_app.models import Movie, UserProfile


class Ticket(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.SET_NULL,null=True)
    price = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    place = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    userprofile = models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)


class Area(models.Model):
    name = models.CharField(max_length=50)


class Places(models.Model):
    number = models.PositiveIntegerField(default=0)
    area = models.ForeignKey(Area,on_delete=models.SET_NULL,null=True)


class TicketPlace(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Places,on_delete=models.SET_NULL,null=True)
    status = models.CharField(choices=(
        ('Free','Free'),
        ('Close','Close'),
    ),max_length=50)

