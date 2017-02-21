from django.contrib import admin

from models import Course, Faculty, Speciality, \
    Specialization, Teacher, Subject, File, Student

admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Speciality)
admin.site.register(Specialization)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(File)
admin.site.register(Student)
