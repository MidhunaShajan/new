# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Department, Course

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]
PURPOSE_CHOICES = [
    ('enquiry', 'For enquiry'),
    ('registration', 'For registration'),
]
# MATERIAL_CHOICES = [
#     ('laptop', 'Laptop'),
#     ('books', 'Books'),
#     ('stationery', 'Stationery'),
# ]


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField()
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(),
    )
    phone_number = forms.CharField(max_length=10)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    purpose = forms.ChoiceField(
        choices=PURPOSE_CHOICES,
        widget=forms.Select,
    )
    materials_provided = forms.MultipleChoiceField(
        choices=[('paper', 'Exam papers'), ('books', 'Books'), ('stationery', 'Stationery')],
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()
        self.fields['department'].widget.attrs.update({'id': 'department-dropdown'})
        self.fields['course'].widget.attrs.update({'id': 'course-dropdown'})

    def save(self):
        pass
class RegistrationForm1(UserCreationForm):


    class Meta:
        model = User
        fields = ['username']