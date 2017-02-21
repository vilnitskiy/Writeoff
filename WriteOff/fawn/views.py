from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User

from .forms import addUserMultiForm


class addUser(CreateView):
    form_class = addUserMultiForm
    template_name = "registration/register.html"
    success_url = '/'

    def form_valid(self, form):
        user = form['user'].save()
        student = form['student'].save(commit=False)
        student.user = User.objects.get(username = user.username)
        student.save()
        return redirect(self.success_url)


def main(request):
    return render(request, 'main.html', {})


def faculties(request):
    return render(request, 'faculties.html', {})
