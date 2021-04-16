from django.shortcuts import render
from rest_framework import views,status
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.


class TicketView(views.APIView):

    def get(self,request,*arqs,**kwargs):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)


class AreaView(views.APIView):

    def get(self, request, *arqs, **kwargs):
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)


class PlacesView(views.APIView):

    def get(self,request,*arqs,**kwargs):
        places = Places.objects.all()
        serializer = PlaceSerializer(places,many=True)
        return Response(serializer.data)

