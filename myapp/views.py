from django.shortcuts import render,redirect

from .models import Student
from .forms import StudentForm
from .models import BloodRequest

# Create your views here.

def list_student(request):
    students= Student.objects.all()
    print(request.GET)
    form =StudentForm()
    data ={
        'students':students
    }
    return render(request,"list_student.html",data)

def delete_student(request,id):
    student =Student.objects.get(id=id)
    
    student.delete()
    return redirect('/list_students/')
    
    

def update_student(request,id):
    print(id)
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    data ={
        'form':form
    }
    return render(request,"update.html",data)


def create_student(request):
    
    print(request.POST)
    form= StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()#saves the student data in the database.
            return redirect('/list_students/')
        
    data ={
        'form':form
    }
    return render(request,"create_student.html",data)

def bloodRequest(request):
    
    blood_requests= BloodRequest.objects.filter(is_expired = False, is_verified = True)
    data ={
        'blood_requests':blood_requests
    }
    return render(request,'blood.html',data)
    
    
 def contact_view(request):
      if request.method == 'POST':
          
     return render(request,'contact.html')   