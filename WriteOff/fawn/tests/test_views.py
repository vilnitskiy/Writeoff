from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

from fawn.models import Course, Faculty, Specialization, Student, Speciality, File
from django.core.files.uploadedfile import SimpleUploadedFile


class TestView(TestCase):
    fixtures = [
        'courses.json',
        'faculties.json',
        'specialities.json',
        'specializations.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='user', password='test')

    def test_home(self):
        """test home view"""
        self.url = reverse('main')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('Log in', response.content)
        self.assertIn('Sign up', response.content)
        self.assertIn('Go to the shit', response.content)

    def test_faculties_view(self):
        """test faculties view"""
        response = self.client.get(reverse('faculties'))
        faculties = Faculty.objects.all()
        self.assertEqual(list(response.context['faculties']), list(faculties))

    def test_courses_view(self):
        """test courses view"""
        response = self.client.get(reverse('courses', kwargs={'id_faculty': 17}))
        courses = Course.objects.all()
        self.assertEqual(list(response.context['courses']), list(courses))
        faculty = Faculty.objects.get(id=17)
        self.assertIn('Your faculty is %s. Now choose your course:' %
                      faculty.name.encode('utf-8'),
                      response.content)

    def test_speciality_view(self):
        """test speciality view"""
        response = self.client.get(reverse('speciality', kwargs={
            'id_faculty': 17,
            'id_course': 2
        }))
        specialities = Speciality.objects.all()
        self.assertEqual(
            list(response.context['specialities']),
            list(specialities))
        faculty = Faculty.objects.get(id=17)
        course = Course.objects.get(id=2)
        self.assertIn('Your faculty is %s, your course is %s course' % (
            faculty.name.encode('utf-8'),
            str(course.course)),
            response.content)

    def test_specialization_view(self):
        """test specialization view"""
        response = self.client.get(reverse('specialization', kwargs={
            'id_faculty': 17,
            'id_course': 2,
            'id_speciality': 4
        }))
        speciality = Speciality.objects.get(id=4)
        specializations = Specialization.objects.filter(speciality=speciality)
        self.assertEqual(
            list(response.context['specializations']),
            list(specializations))
        faculty = Faculty.objects.get(id=17)
        course = Course.objects.get(id=2)
        self.assertIn(
            'Your faculty is %s, your course is %s course, your speciality is %s.' % (
                faculty.name.encode('utf-8'),
                str(course.course),
                speciality.name.encode('utf-8')),
            response.content)


class TestForm(TestCase):
    fixtures = [
        'courses.json',
        'faculties.json',
        'specialities.json',
        'specializations.json']

    def setUp(self):
        self.client = Client()
        User.objects.create(username='user', password='test')
        self.client.login(username="user", password="test")
        self.faculty = Faculty.objects.get(id=2)
        self.course = Course.objects.get(id=2)
        self.speciality = Speciality.objects.get(id=2)
        self.specialization = Specialization.objects.get(id=3)
        self.url = reverse('files', kwargs={
            'id_faculty': 2,
            'id_course': 2,
            'id_speciality': 2,
            'id_specialization': 3
        })

    def test_post_form(self):
        """check saving data"""
        response = self.client.post(self.url, {
            "file": SimpleUploadedFile('lol.txt', 'lol'),
            "subject": "qwert",
            "file_type": "controlw",
            "extra_comment": "lolololo",
            "specialization": self.specialization.id,
            "course": self.course.id,
            "faculty": self.faculty.id,
        }, follow=True)
        self.assertEqual(File.objects.count(), 1)
        self.assertEqual(response.context['success'], 1)

    def test_displaying_form(self):
        """check displaying form"""
        response = self.client.get(self.url)
        self.assertIn('File:', response.content)
        self.assertIn('Subject:', response.content)
        self.assertIn('File type:', response.content)
        self.assertIn('Extra comment:', response.content)
        self.assertIn('Specialization:', response.content)
        self.assertIn('Course', response.content)
        self.assertIn('Faculty', response.content)


class TestRegistrationView(TestCase):
    fixtures = [
        'courses.json',
        'faculties.json',
        'specialities.json',
        'specializations.json']

    def setUp(self):
        self.client = Client()
        self.url = reverse('register')

    def test_displaying_form(self):
        """check displaying form"""
        response = self.client.get(self.url)
        self.assertIn('Username:', response.content)
        self.assertIn('Password:', response.content)
        self.assertIn('Password confirmation:', response.content)
        self.assertIn('Faculty:', response.content)
        self.assertIn('Group:', response.content)
        self.assertIn('Course', response.content)
        self.assertIn('Specialization', response.content)

    def test_post_form(self):
        """check saving data"""
        response = self.client.post(self.url, {
            "user-username": "Lollol1",
            "user-password1": "pbkdf2_sha256$30000$8W2dhItA8If2$C1pAmCP/OLYR7CppsM9PM+2pYybA6P6qBuoiTwU2Hr0=",
            "user-password2": "pbkdf2_sha256$30000$8W2dhItA8If2$C1pAmCP/OLYR7CppsM9PM+2pYybA6P6qBuoiTwU2Hr0=",
            "student-faculty": 1,
            "student-specialization": 1,
            "student-course": 2,
            "student-group": "grupa"
        }, follow=True)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Student.objects.count(), 1)
        self.assertRedirects(response, expected_url=reverse('main'), status_code=302)

