from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from betterforms.multiform import MultiModelForm

from .models import Student, File


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields = ('faculty', 'course', 'specialization', 'group')


class RegistrationMultiForm(MultiModelForm):
    form_classes = {
        'user': UserRegistrationForm,
        'student': StudentRegistrationForm,
    }


class FileUploadForm(ModelForm):
    class Meta:
        model = File
        fields = '__all__'

