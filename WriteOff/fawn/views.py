from django.shortcuts import render


def main(request):
    return render(request, 'main.html', {})


def faculties(request):
    return render(request, 'faculties.html', {})
