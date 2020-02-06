from django.shortcuts import render
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

def meetingDetails(request):
    meetDt=get_object_or_404(Meeting, pk=meetingtitle)
    date=Meeting.meetingdate
    location=Meeting.location
    context={
        'meetDT':meetDt,
        'date':date,
        'location':location,
    }
    return render(request, 'Club/meetingDetail.html', context=context)
