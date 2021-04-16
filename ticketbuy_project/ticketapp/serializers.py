from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from ticketbuy_app.serializers import MovieSerializer,UserProfileSerializer


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['price','start_time','end_time','place','area']


class AreaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)

    class Meta:
        model = Area
        fields = ['name',]


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Places
        fields =['number','area',]
