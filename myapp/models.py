from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
class Customer (models.Model):
    name = models.CharField(max_length=100)
    phone_number =models.IntegerField()
    address = models.CharField(max_length=255)    
    email = models. CharField(max_length=50)
    secondary_phone= models.CharField(max_length=10, null=True)
    
class BloodRequest(models.Model):
    bloodchoices =(
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),

    )
    
    title = models.CharField(max_length=100)
    patients_name = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    requirement_reason = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=20, choices=bloodchoices)
    contact_number = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=True)
    is_expired = models.BooleanField(default=False)
    requirement_date = models.DateTimeField(null=True, blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    