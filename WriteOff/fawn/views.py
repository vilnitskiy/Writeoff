from django.shortcuts import render


def main(request):
    return render(request, 'main.html', {})


def faculties_list(request):
    return render(request, 'faculties.html', {})
