from django.shortcuts import render,get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request,'Club/index.html')
def getResource(request):
    resource_list = Resource.objects.all()
    context={'resource_list':resource_list}
    return render(request, 'Club/resource.html', context=context)

def getMeeting(request):
    meeting_list = Meeting.objects.all()
    context={'meeting_list':meeting_list}
    return render(request, 'Club/meeting.html', context=context)

def getEvent(request):
    event_list = Event.objects.all()
    context={'event_list':event_list}
    return render(request, 'Club/event.html', context=context)

def meetingDetails(request,id):
    meet=get_object_or_404(Meeting, pk=id)
    date = meet.meetingdate
    time = meet.meetingtime
    location = meet.location
    agenda = meet.agenda
    context={
        'meet':meet,
        'date':date,
        'time':time,
        'location':location,
        'agenda':agenda,
    }
    return render(request, 'Club/meetingDetail.html', context=context)

def eventDetails(request,id):
    eve=get_object_or_404(Event, pk=id)
    uid = eve.userid
    date = eve.date
    time = eve.time
    location = eve.location
    description = eve.description
    context={
        'eve':eve,
        'uid':uid,
        'date':date,
        'time':time,
        'location':location,
        'description':description,
    }
    return render(request, 'Club/eventDetail.html', context=context)
