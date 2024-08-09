from django.urls import path
from .views import *
from myapp.views import *

urlpatterns = [
    path('list_students/',list_student),
    path('create_student/',create_student),
    path('update/<int:id>/',update_student),
    path('delete/<int:id>/',delete_student),
    path('blood/',bloodRequest),
    path('contact/',contact)
    #localhost:8080/update/1/
    
]
