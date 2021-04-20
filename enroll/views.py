import django
from django.core.exceptions import RequestDataTooBig
from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from .models import NewUser
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            fname=form.cleaned_data['first_name']
            lname=form.cleaned_data['last_name']
            pasword=form.cleaned_data['password']
            pst = NewUser(first_name=fname,last_name=lname,password=pasword)
            pst.save()
            messages.success(request,'Congratulation!!!')
            return HttpResponseRedirect('/login/')
    else:
        form = SignUpForm()
    return render(request,'enroll/signup.html',{'form':form})



def login(request):
        data=request.POST
        form = LoginForm()
        
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            pasword= form.cleaned_data['password']
            user = NewUser(first_name=fname, password=pasword)
            print(fname,pasword)
            if user is not None:
                login(user)
    
        return render(request,'enroll/login.html',{'form':form})
