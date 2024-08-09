from django.contrib import admin
from myapp.models import Student
from myapp.models import Customer,BloodRequest
# Register your models here.

admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(BloodRequest)