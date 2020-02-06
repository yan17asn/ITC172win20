from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingdate = models.DateField()
    meetingtime = models.TimeField()
    location = models.CharField(max_length=255)
    agenda = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'
        verbose_name_plural='meeting'

class MeetingMinutes(models.Model):
    meetingid = models.ForeignKey(Meeting,on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.minutes
    
    class Meta:
        db_table='meetingminutes'
        verbose_name_plural='meetingminutes'

class Resource(models.Model):
    resourcename = models.CharField(max_length=255)
    resourcetype = models.CharField(max_length=255)
    url = models.URLField(null=True,blank=True)
    dateentered = models.DateField()
    userid = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'
        verbose_name_plural='resource'

class Event(models.Model):
    eventtitle = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(null=True, blank=True)
    userid = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'
        verbose_name_plural='event'



