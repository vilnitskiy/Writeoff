from django.shortcuts import render

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
