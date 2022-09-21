from django.urls import path
from ResumeApp import views

urlpatterns=[
    path("",views.personal,name="home"),
    path("residence/",views.residence,name="residence"),
    path("designation/",views.designation,name="designation"),
    path("education/",views.education,name="education"),
    path("resume/",views.resume,name="resume")
]