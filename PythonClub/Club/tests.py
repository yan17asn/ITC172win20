from django.test import TestCase
from django.urls import reverse
from .models import Meeting, MeetingMinutes, Resource, Event
from django.contrib.auth.models import User

# Create your tests here.
# ==================  Meeting Model ========================

class MeetingTest(TestCase):
   #test string
    def setUp(self):
       meeting = Meeting(meetingtitle='Python Introduction',location='Seattle Central',
       agenda='Python meeting agenda 02122020')
       return meeting
    
    def test_string(self):
       meet = self.setUp()
       self.assertEqual(str(meet), meet.meetingtitle)

    def test_location(self):
       meet = self.setUp()
       self.assertEqual(str(meet.location),'Seattle Central')

    def test_agenda(self):
       meet = self.setUp()
       self.assertEqual(str(meet.agenda),'Python meeting agenda 02122020')

   # test Meeting table.
    def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')

# ==================  MeetingMinutes Model ========================

class MeetingMinutesTest(TestCase):
   #test string
    def setUp(self):
       title = Meeting(meetingtitle='Python Introduction')
       minute = MeetingMinutes(meetingid=title,minutes='meeting minute 02122020')
       return minute
    
    def test_string(self):
       min = self.setUp()
       self.assertEqual(str(min), min.minutes)
    
    def test_title(self):
       min = self.setUp()
       self.assertEqual(str(min.meetingid),'Python Introduction')
   
   # test MeetingMinutes table.
    def test_table(self):
       self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

# ==================  Resource Model ========================

class ResourceTest(TestCase):
   #test string
    def setUp(self):
       resource = Resource(resourcename='Python resource 001', resourcetype='PDF',
       description='Python example source code')
       return resource

    def test_string(self):
       res = self.setUp()
       self.assertEqual(str(res), res.resourcename)

    def test_type(self):
       res = self.setUp()
       self.assertEqual(str(res.resourcetype),'PDF')

    def test_description(self):
       res = self.setUp()
       self.assertEqual(str(res.description),'Python example source code')
   

# test Resource table.
    def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')

# ==================  Event Model ========================

class EventTest(TestCase):
   #test string
    def setUp(self):
       event = Event(eventtitle='Django introduction',location='Seattle Central',
       description='Introduce django frame')
       return event

    def test_string(self):
       eve = self.setUp()
       self.assertEqual(str(eve), eve.eventtitle)

    def test_location(self):
       eve = self.setUp()
       self.assertEqual(str(eve.location), 'Seattle Central')

    def test_description(self):
       eve = self.setUp()
       self.assertEqual(str(eve.description),'Introduce django frame')

# test Event table.
    def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'event')


# ==================  View_url Test ========================
        

class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response=self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)

class ResourceViewTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response=self.client.get(reverse('resource'))
       self.assertEqual(response.status_code, 200)

class MeetingViewTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response=self.client.get(reverse('meeting'))
       self.assertEqual(response.status_code, 200)

class EventViewTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response=self.client.get(reverse('event'))
       self.assertEqual(response.status_code, 200)

class DetailPageTest(TestCase):
   def setUp(self):
       self.u = User.objects.create(username='User001')
       self.event = Event.objects.create(eventtitle='Django introduction',date='2020-02-12',time='05:00',location='Seattle Central',
       description='Introduce django frame',userid=self.u)
       self.meet = Meeting.objects.create(meetingtitle='Python Introduction',meetingdate='2020-02-12',meetingtime='06:00',location='Seattle Central',
       agenda='Python meeting agenda 02122020')
       
        
   def test_event_detail_success(self):
        response = self.client.get(reverse('eventdetail', args=(self.event.id,)))
        self.assertEqual(response.status_code, 200)

   def test_meeting_detail_success(self):
        response = self.client.get(reverse('meetingdetail', args=(self.meet.id,)))
        self.assertEqual(response.status_code, 200)

class New_Resource_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.resource = Resource(resourcename='Python resource 001', resourcetype='PDF',
       description='Python example source code')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/newResource/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newresource'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/newResource.html')

class New_Meeting_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.meet = Meeting.objects.create(meetingtitle='Python Introduction',meetingdate='2020-02-12',meetingtime='06:00',location='Seattle Central',
       agenda='Python meeting agenda 02122020')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/newMeeting/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/newMeeting.html')

