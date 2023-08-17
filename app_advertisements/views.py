from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm


# Create your views here.
def index(request):
    advertisements=Advertisement.objects.all()
    context={'advertisements':advertisements}
    return render(request,'index.html',context)

def top_sellers(request):
    return render(request,'top-sellers.html')

def advertisement_post(request):
    if request.method=='POST':
        form=AdvertisementForm(request.POST,request.FILES)
        if form.is_valid():
            advertisement=Advertisement(**form.cleaned_data)
            if request.user.is_authenticated:
                advertisement.user=request.user
            advertisement.save()
            url=reverse('index')
            return redirect(url)
    else:
        form=AdvertisementForm()
    context={'form':form}
    return render(request,'advertisement-post.html',context)

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')



