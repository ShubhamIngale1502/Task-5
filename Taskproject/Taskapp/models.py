from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    
    GENDER = [
        ('male','male'),
        ('female','female'),
        ('other','other')
    ]
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length=45, blank=True)
    gender = models.CharField(max_length=40, choices = GENDER)
    contact = PhoneNumberField(blank=True,region = 'IN') 
    address = models.TextField()
    city = models.CharField(max_length = 45)
    pincode = models.IntegerField()
    profile_pic =  models.ImageField(upload_to='profile_pic')
