import logging

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

from .forms import RegistrationMultiForm, FileUploadForm
from fawn.models import Faculty, File, Course, Student


logger = logging.getLogger(__name__)


class RegistrationView(CreateView):
    """ Custom view for registering students """
    form_class = RegistrationMultiForm
    template_name = 'registration/register.html'
    success_url = 'uploaded_files'

    def form_valid(self, form):
        user = form['user'].save()
        student = form['student'].save(commit=False)
        student.user = User.objects.get(username=user.username)
        student.save()
        new_user = authenticate(username=form['user'].cleaned_data['username'],
                                password=form['user'].cleaned_data['password1'])
        login(self.request, new_user)

        return redirect(reverse(self.success_url, kwargs={
            'id_faculty': student.faculty.id,
            'id_course': student.course.id
        }))


class FilesView(View):
    form_class = FileUploadForm
    initial = {}
    template_name = 'files.html'

    def get(self, request, *args, **kwargs):
        # extracting parameters to get queryset
        files_queryset = File.objects.filter(faculty=kwargs['id_faculty'],
                                             course=kwargs['id_course']
                                             )
        # passing initial data to FileUpload form
        self.initial['faculty'] = kwargs['id_faculty']
        self.initial['course'] = kwargs['id_course']

        form = self.form_class(initial=self.initial)
        data = {
            'files': files_queryset,
            'form': form,
            'chosen_faculty': kwargs['id_faculty'],
            'chosen_course': kwargs['id_course']
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('uploaded_files', kwargs={
            'id_faculty': kwargs['id_faculty'],
            'id_course': kwargs['id_course']
            }))
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


def uploaded_files(request, **kwargs):
    faculty = Faculty.objects.get(id=kwargs['id_faculty'])
    course = Course.objects.get(id=kwargs['id_course'])

    files_queryset = File.objects.filter(faculty=faculty,
                                         course=course
                                         )

    return render(request, 'uploaded_files.html',
                  {
                      'files': files_queryset,
                      'chosen_faculty': faculty,
                      'chosen_course': course
                  })
