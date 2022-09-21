from dataclasses import field
from datetime import datetime
from socket import fromshare
from django import forms

from ResumeApp.models import Designation, Education, Residence, Resume

gender_choice=(
    ('Male','Male'),
    ('Female','Female')
)

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=gender_choice,widget=forms.RadioSelect)

    class Meta:
        model=Resume
        fields="__all__"
        labels={'firstname':'Enter FirstName',
        'lastname':'Enter LastName',
        'gender':'Enter Gender',
        'dob':'Enter DOB',
        'phone':'Enter PhoneNo.',
        'email':'Enter Mail'}

class ResidenceForm(forms.ModelForm):
    class Meta:
        model=Residence
        fields="__all__"
        labels={'state':'Select State','city':'Enter City','pin':'Enter Pin-Code','address':'Enter Address'}


skill_choices=(
    ("java","java"),
    ("python","python"),
    ("C++","C++"),
    ("Django","Django"),
    ("React","React"),
    ("Javascript","Javascript"),
    ("Salesforce","Salesforce"),

)

class DesignationForm(forms.ModelForm):
    skills=forms.MultipleChoiceField(choices=skill_choices,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Designation
        fields="__all__"

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields="__all__"
        