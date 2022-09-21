from django.contrib import admin

from ResumeApp.models import Designation, Education, Residence, Resume

# Register your models here.
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['id','firstname','lastname','gender','dob','phone','email']


@admin.register(Residence)
class ResidenceAdmin(admin.ModelAdmin):
    list_display=['state','city','pin','address']


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display=["role","skills","photo"]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass