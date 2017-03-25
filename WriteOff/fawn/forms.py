from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from betterforms.multiform import MultiModelForm

from .models import Student, File


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields = ('faculty', 'course', 'specialization', 'group')

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['faculty'].widget.attrs['class'] = 'form-control'
        self.fields['course'].widget.attrs['class'] = 'form-control'
        self.fields['specialization'].widget.attrs['class'] = 'form-control'
        self.fields['group'].widget.attrs['class'] = 'form-control'


class RegistrationMultiForm(MultiModelForm):
    form_classes = {
        'user': UserRegistrationForm,
        'student': StudentRegistrationForm,
    }


class FileUploadForm(ModelForm):
    class Meta:
        model = File
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)

        self.fields['file'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['file_type'].widget.attrs['class'] = 'form-control'
        self.fields['extra_comment'].widget.attrs['class'] = 'form-control'
        self.fields['specialization'].widget.attrs['class'] = 'form-control'
        self.fields['course'].widget.attrs['class'] = 'form-control'
        self.fields['faculty'].widget.attrs['class'] = 'form-control'
