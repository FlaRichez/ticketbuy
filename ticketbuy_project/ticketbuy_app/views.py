from django.shortcuts import render
from rest_framework import views,status
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.


class RegisterView(views.APIView):

    def post(self,request,*args,**kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class MovieView(views.APIView):

    def get(self,request,*arqs,**kwargs):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)



