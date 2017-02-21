from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse

from .forms import RegistrationMultiForm


class RegistrationView(CreateView):
    """ Custom view for registering students """
    form_class = RegistrationMultiForm
    template_name = 'registration/register.html'
    success_url = 'main'

    def form_valid(self, form):
        user = form['user'].save()
        student = form['student'].save(commit=False)
        student.user = User.objects.get(username = user.username)
        student.save()
        return redirect(reverse(self.success_url))

from fawn import models


def main(request):
    return render(request, 'main.html', {})


def faculties(request):
    faculties = models.Faculty.objects.all()
    return render(request, 'faculties.html', {'faculties': faculties})


def courses(request, id):
    courses = models.Course.objects.all()
    chosen_faculty = models.Faculty.objects.get(id=id)
    return render(request, 'courses.html',
                  {'courses': courses,
                   'chosen_faculty': chosen_faculty})


def speciality(request):
    return render(request, 'speciality.html', {})
