from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,logout,login as dj_login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserForm 

# Create your views here.

def register(request):
    redirect_url=reverse('profile')
    if request.method=="POST":
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(request,username=username,password=password)
            dj_login(request, user)
            return redirect(redirect_url)
    else:
        form= UserForm()
    return render(request,'app_user/register.html',{'form':form})

def login(request):
    redirect_url=reverse('profile')
    if request.method=="GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request,'app_user/login.html')
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        dj_login(request, user)
        return redirect(redirect_url)
    return render(request,'app_user/login.html',{'error':'Пользователь не найден'})
        
@login_required(login_url=reverse_lazy('login'))
def profile(request):
    return render(request,'app_user/profile.html')

def logout_w(request):
    logout(request)
    return redirect(reverse('login'))


