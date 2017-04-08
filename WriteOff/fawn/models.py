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

    def __unicode__(self):
        return u"%d course" % (self.course)


class Faculty(models.Model):
    name = models.CharField(max_length=10)
    full_name = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u"%s" % (self.name)


class File(models.Model):
    file = models.FileField()
    subject = models.CharField(max_length=60)
    file_type = models.CharField(
        choices=Constants.TYPE_CHOICES,
        max_length=100)
    extra_comment = models.TextField()
    course = models.ForeignKey(Course)
    faculty = models.ForeignKey(Faculty)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # custom fields
    faculty = models.ForeignKey(Faculty, null=True, blank=True)
    course = models.ForeignKey(Course, null=True, blank=True)
    group = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return u"%s %s" % (self.user.username, self.faculty)
