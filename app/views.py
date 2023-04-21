from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from app.models import *
def student(request):
    SFO = StudentForm()
    d={'SFO':SFO}
    if request.method == 'POST':
        SFD = StudentForm(request.POST) 
        if SFD.is_valid():
            name = SFD.cleaned_data.get('name')
            age = SFD.cleaned_data.get('age')
            email = SFD.cleaned_data.get('email')
            date = SFD.cleaned_data.get('date')
            password = SFD.cleaned_data.get('password')
            address = SFD.cleaned_data.get('address')
            gender = SFD.cleaned_data.get('gender')
            course = SFD.cleaned_data.get('course')
              
            SO=Student.objects.get_or_create(name=name,age=age,email=email,date=date,password=password,address=address,gender=gender,course=course)[0]
            SO.save()

            return HttpResponse("your data is saved successfully")




    return render(request,'student.html',d)