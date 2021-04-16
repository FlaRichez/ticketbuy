from django.urls import path
from .views import *

urlpatterns = [
    path('ticket',TicketView.as_view()),
    path('area/',AreaView.as_view()),
    path('place/',PlacesView.as_view()),
]