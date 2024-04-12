from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'phone', 'address', 'compensation', 'salary', 'department']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddEmployeeForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['department'].queryset = Department.objects.filter(user=user)



class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'




class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title']


class AddAssignmentsForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['employee', 'position', 'begin_date', 'end_date']

    def __init__(self, user, *args, **kwargs):
        super(AddAssignmentsForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(user=user)
        self.fields['position'].queryset = Job.objects.filter(user=user)


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }