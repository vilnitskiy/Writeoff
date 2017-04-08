from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views

from fawn import forms, views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main, name='main'),

    # Steps for unauthed user
    url(r'^faculties/', views.faculties, name='faculties'),
    url(r'^(?P<id_faculty>\d+)/course/', views.courses, name='courses'),
    #url(r'^(?P<id_faculty>\d+)/(?P<id_course>\d+)/speciality/',
    #    views.speciality,
    #    name='speciality'),
    #url(r'^(?P<id_faculty>\d+)/(?P<id_course>\d+)/(?P<id_speciality>\d+)/specialization/',
    #    views.specialization,
    #    name='specialization'),
    url(r'^(?P<id_faculty>\d+)/(?P<id_course>\d+)/',
        views.FilesView.as_view(),
        name='files'),
    url(r'^uploaded_files/(?P<id_faculty>\d+)/(?P<id_course>\d+)/',
        views.uploaded_files,
        name='uploaded_files'),

    # auth views
    url('^register/', views.RegistrationView.as_view(), name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
