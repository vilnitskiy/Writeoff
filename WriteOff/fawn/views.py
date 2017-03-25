import logging

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import Http404

from .forms import RegistrationMultiForm, FileUploadForm
from fawn.models import Faculty, Speciality, File, Specialization, Course, Student, Subject, Teacher


logger = logging.getLogger(__name__)


class RegistrationView(CreateView):
    """ Custom view for registering students """
    form_class = RegistrationMultiForm
    template_name = 'registration/register.html'
    success_url = 'main'

    def form_valid(self, form):
        user = form['user'].save()
        student = form['student'].save(commit=False)
        student.user = User.objects.get(username=user.username)
        student.save()
        new_user = authenticate(username=form['user'].cleaned_data['username'],
                                password=form['user'].cleaned_data['password1'])
        login(self.request, new_user)
        return redirect(reverse(self.success_url))


class FilesView(View):
    form_class = FileUploadForm
    initial = {}
    template_name = 'files.html'

    def get(self, request, *args, **kwargs):
        # extracting parameters to get queryset
        faculty = Faculty.objects.get(id=kwargs['id_faculty'])
        course = Course.objects.get(id=kwargs['id_course'])
        specialization = Specialization.objects.get(
            id=kwargs['id_specialization']
        )

        files_queryset = File.objects.filter(faculty=faculty,
                                             course=course,
                                             specialization=specialization)

        # passing initial data to FileUpload form
        self.initial['faculty'] = faculty
        self.initial['course'] = course
        self.initial['specialization'] = specialization

        form = self.form_class(initial=self.initial)
        data = {
            'files': files_queryset,
            'form': form,
            'chosen_specialization': kwargs['id_specialization'],
            'chosen_faculty': kwargs['id_faculty'],
            'chosen_course': kwargs['id_course'],
            'chosen_speciality': kwargs['id_speciality']
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'success': True,
                                                        'form': form})
        return render(request, self.template_name, {'success': False,
                                                    'form': form})


def main(request):
    return render(request, 'main.html', {})


def faculties(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculties.html', {'faculties': faculties})


def courses(request, id_faculty):
    courses = Course.objects.all()
    try:
        chosen_faculty = Faculty.objects.get(id=id_faculty)
    except:
        logger.error('Cannot get model instance')
        raise Http404
    return render(request, 'courses.html',
                  {'courses': courses,
                   'chosen_faculty': chosen_faculty})


def speciality(request, id_faculty, id_course):
    specialities = Speciality.objects.all()
    try:
        chosen_faculty = Faculty.objects.get(id=id_faculty)
        chosen_course = Course.objects.get(id=id_course)
    except:
        logger.error('Cannot get model instance')
        raise Http404
    return render(request, 'specialities.html',
                  {'specialities': specialities,
                   'chosen_faculty': chosen_faculty,
                   'chosen_course': chosen_course})


def specialization(request, id_faculty, id_course, id_speciality):
    specializations = Specialization.objects.all()
    try:
        chosen_faculty = Faculty.objects.get(id=id_faculty)
        chosen_course = Course.objects.get(id=id_course)
        chosen_speciality = Speciality.objects.get(id=id_speciality)
    except:
        logger.error('Cannot get model instance')
        raise Http404
    return render(request, 'specializations.html',
                  {'specializations': specializations,
                   'chosen_faculty': chosen_faculty,
                   'chosen_course': chosen_course,
                   'chosen_speciality': chosen_speciality})


def subjects(request, id_faculty, id_course, id_speciality):
    faculty = Faculty.objects.get(id=kwargs['id_faculty'])
    course = Course.objects.get(id=kwargs['id_course'])
    specialization = Specialization.objects.get(
        id=kwargs['id_specialization']
    )
    files_queryset = File.objects.filter(faculty=faculty,
                                         course=course,
                                         specialization=specialization)
    subjects = files_queryset.subject
    return render(request, 'subjects.html', {'subjects': subjects})