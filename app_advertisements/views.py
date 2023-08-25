from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    advertisements=Advertisement.objects.all()
    context={'advertisements':advertisements}
    return render(request,'app_advertisements/index.html',context)

def top_sellers(request):
    return render(request,'app_advertisements/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
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
    return render(request,'app_advertisements/advertisement-post.html',context)




