import email
from django.db import models

# Create your models here.
class Resume(models.Model):
    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    gender=models.CharField(max_length=15)
    dob=models.DateField()
    phone=models.IntegerField()
    email=models.EmailField()

    
class Residence(models.Model):
    state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    state=models.CharField(max_length=50,choices=state_choices)
    city=models.CharField(max_length=50)
    pin=models.IntegerField()
    address=models.TextField(max_length=150)

class Designation(models.Model):
    role_choices=(("FrontEnd","FrontEnd"),("BackEnd","BackEnd"),("FullStack","FullStack"))
    role=models.CharField(choices=role_choices,max_length=50)
    skills=models.CharField(max_length=50)
    photo=models.ImageField(upload_to="photo")

class Education(models.Model):
    graduation=models.CharField(max_length=50)
    higher=models.CharField(max_length=50)
    secondary=models.CharField(max_length=50)
    degreemarks=models.FloatField()
    highermarks=models.FloatField()
    secondarymarks=models.FloatField()
    degreedate=models.DateField()
    higherdate=models.DateField()
    secondarydate=models.DateField()