from django.shortcuts import HttpResponse, render

from random import randint

def index_view(request):
    random_data = randint(1,100)
    
    
    data= {
        "name":"SAGAR ADHIKARI",
        "age":22,
        "gender":"Male",
        "random":random_data,
        "hobbies":["Singing","Dancing","Gaming"]
 }
    
    # return HttpResponse("This is index page")
    return render(request,"index.html",data)
    

def login_view(request):
    # return HttpResponse("This is login page")
    return render(request,"login.html")

def register_view(request):
    # return HttpResponse("This is register page")
    return render(request,"register.html")

