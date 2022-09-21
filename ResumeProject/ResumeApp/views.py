from django.shortcuts import render,redirect

from ResumeApp.forms import DesignationForm, EducationForm, ResidenceForm, ResumeForm
from ResumeApp.models import Designation, Education, Residence, Resume

# Create your views here.
def personal(request):
    if request.method=="POST":
        form=ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("residence")
    form=ResumeForm()
    template_name='personal.html'
    context={'form':form}
    return render(request,template_name,context)

def residence(request):
    if request.method=="POST":
        form=ResidenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('designation')
    form=ResidenceForm()
    template_name='residence.html'
    context={'form':form}
    return render(request,template_name,context)

def designation(request):
    if request.method=="POST":
        form=DesignationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("education")
    form=DesignationForm()
    template_name='designation.html'
    context={'form':form}
    return render(request,template_name,context)

def education(request):
    if request.method=="POST":
        form=EducationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume')
    form=EducationForm()
    template_name='education.html'
    context={'form':form}
    return render(request,template_name,context)

def resume(request):
    personal=Resume.objects.all()
    residence=Residence.objects.all()
    education=Education.objects.all()
    designation=Designation.objects.all()
    template_name='resume.html'
    context={'personal':personal,'residence':residence,'education':education,'designation':designation}
    return render(request,template_name,context)
    
