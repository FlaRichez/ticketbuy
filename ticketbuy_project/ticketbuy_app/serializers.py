from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8,max_length=16)
    confirm_password = serializers.CharField(min_length=8,max_length=16)
    username = serializers.CharField(min_length=4)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password','confirm_password']

    def create(self, validated_data):
        password = validated_data.pop('password') #1
        confirm_password = validated_data.pop('confirm_password') #1
        if password != confirm_password:
            raise ValidationError({"data":"Passwords don't match!"})
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user,email=user.email,
                                   full_name=user.first_name.capitalize() + " " + user.last_name.capitalize())
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id','user','full_name','phone','email',]


class MovieSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=500)
    average_rate = serializers.FloatField(min_value=1,max_value=10)

    class Meta:
        model = Movie
        fields = ['name','description','average_rate']




