from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth.models import User
from django.urls import reverse

from .forms import RegistrationMultiForm, FileUploadForm
from fawn.models import *


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
        return redirect(reverse(self.success_url))


class FilesView(View):
    form_class = FileUploadForm
    initial = {}
    # template_name = 'form_template.html'

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
            'form': form
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponse({'success': True})

        return render(request, '', {'form': form})


def main(request):
    return render(request, 'main.html', {})


def faculties(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculties.html', {'faculties': faculties})


def courses(request, id_faculty):
    courses = Course.objects.all()
    chosen_faculty = Faculty.objects.get(id=id_faculty)
    return render(request, 'courses.html',
                  {'courses': courses,
                   'chosen_faculty': chosen_faculty})


def speciality(request, id_faculty, id_course):
    return render(request, 'speciality.html', {})


def specialization(equest, id_faculty, id_course, id_speciality):
    pass
