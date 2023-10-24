from django.test import TestCase, Client
from django.utils import timezone
from datetime import datetime,timedelta
from .models import Bug
from django.urls import reverse


# Create your tests here.


class BugModelTests(TestCase):
     def test_create_bug(self):
        bug = Bug.objects.create(
            description="AttributeError",
            bug_type="error",
            report_date=timezone.now(),
            status="todo"
        )
        self.assertIsInstance(bug, Bug)
        self.assertEqual(bug.description, "AttributeError")
        self.assertEqual(bug.bug_type, "error")
        self.assertEqual(bug.status, "todo")

     def test_bug_type(self):
        bug = Bug.objects.create(
            description="AttributeError",
            bug_type="error",
            report_date="2023-10-18",
            status="todo"
        )
        self.assertIn(bug.bug_type, dict(Bug.BUG_TYPES).keys())

     def test_bug_status(self):
        bug = Bug.objects.create(
            description="AttributeError",
            bug_type="error",
            report_date="2023-10-18",
            status="todo"
        )
        self.assertIn(bug.status, dict(Bug.STATUS).keys())

     def test_report_date(self):
        bug = Bug.objects.create(
            description="AttributeError",
            bug_type="error",
            report_date=timezone.now(),
            status="todo"
        )
        self.assertIsNotNone(Bug.report_date)


class IndexViewTest(TestCase):

    def setUp(self):
       
        self.bug = Bug.objects.create(
            description="AttributeError",
            bug_type="error",
            report_date=timezone.now(),
            status="todo"
        )

    def test_list_bug_view(self):
    
        client = Client()
        response = client.get(reverse('list_bug'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_bug.html')

    def test_view_bug_view(self):
       
        response = self.client.get(reverse('view_bug', args=[self.bug.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_bug.html')
        self.assertEqual(response.context['data'], self.bug)

    def test_register_bug_view(self):
    
        client = Client()
        response = client.get(reverse('register_bug'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_bug.html')
