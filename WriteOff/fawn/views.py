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


def main(request):
    return render(request, 'main.html', {})


def faculties(request):
    return render(request, 'faculties.html', {})
