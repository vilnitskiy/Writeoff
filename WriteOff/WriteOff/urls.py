from django.conf.urls import url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views

from fawn import forms, views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main, name='main'),

    # Steps for unauthed user
    url(r'^faculties/', views.faculties, name='faculties'),
    url(r'^(?P<id>\d+)/course/', views.courses, name='courses'),
    url(r'^(?P<id>\d+)/speciality/', views.speciality, name='speciality'),

    # auth views
    url('^register/', views.RegistrationView.as_view(), name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
