from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Constants:
    TYPE_CHOICES = (
        ("labw", ("Lab work")),
        ("controlw", ("Control work")),
        ("calcw", ("Calculation work")),
        ("homew", ("Homework")),
        ("otherw", ("Another type of work"))
    )

class Course(models.Model):
    course = models.PositiveSmallIntegerField()


class Faculty(models.Model):
    name = models.CharField(max_length=10)
    full_name = models.TextField(null=True, blank=True)


class Speciality(models.Model):
    name = models.TextField()


class Specialization(models.Model):
    name = models.TextField()
    speciality = models.ForeignKey(Speciality)


class Teacher(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=False)
    degree = models.CharField(max_length=30, null=True, blank=True)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    full_name = models.TextField()
    teacher = models.ForeignKey(Teacher, blank=True, null=True)


class File(models.Model):
    file = models.FileField()
    subject = models.ForeignKey('Subject')
    type = models.TextField(choices=Constants.TYPE_CHOICES)
    extra_comment = models.TextField()
    specialization = models.ForeignKey(Specialization)
    course = models.ForeignKey(Course)
    faculty = models.ForeignKey(Faculty)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, null=True, blank=True)
    specialization = models.ForeignKey(Specialization, null=True, blank=True)
    course = models.ForeignKey(Course, null=True, blank=True)
    group = models.CharField(max_length=10, null=True, blank=True)
