from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *



def student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}

    if request.method=="POST":
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('invalid data')
        


    return render(request,'student.html',d)
