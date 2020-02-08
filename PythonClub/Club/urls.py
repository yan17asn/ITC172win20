from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getResource/', views.getResource, name="resource"),
    path('getMeeting/', views.getMeeting, name="meeting"),
    path('getEvent/', views.getEvent, name="event"),
    path('getmeetingDetail/<int:id>', views.meetingDetails, name="meetingdetail"),
    path('geteventDetail/<int:id>', views.eventDetails, name="eventdetail"),
]