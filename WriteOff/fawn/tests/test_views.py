from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

from fawn.models import Course, Faculty, Specialization, Student


class TestView(TestCase):
    fixtures = ['courses.json', 'faculties.json', 'specialities.json', 'specializations.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='user', password='test')

    def test_home(self):
        """ test for home view """
        self.url = reverse('main')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('Log in', response.content)
        self.assertIn('Sign up', response.content)
        self.assertIn('Go to the shit', response.content)