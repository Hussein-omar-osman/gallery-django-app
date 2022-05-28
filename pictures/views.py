from django.shortcuts import redirect, render
from .models import Image


# Create your views here.
def homePage(request):
   images = Image.objects.all()
   context = {'images':images}
   return render(request, 'pictures/home.html', context)
  

  
  
