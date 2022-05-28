from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Image
from .forms import ImageForm


# Create your views here.
def homePage(request):
   images = Image.objects.all()
   context = {'images':images}
   return render(request, 'pictures/home.html', context)


def searchPage(request):
   q = request.GET.get('q') if request.GET.get('q') != None else ''

   images = Image.objects.filter(
        Q(name__icontains=q) |
        Q(location__name__icontains=q) |
        Q(category__name__icontains=q)
        )
   if request.method == 'POST':
      q = request.POST.get('search')
      print(q)
      images = Image.objects.filter(
        Q(name__icontains=q) |
        Q(location__name__icontains=q) |
        Q(category__name__icontains=q)
        )
      context = {'images':images, 'q':q}
      return render(request, 'pictures/search_results.html', context)
      
      
   # images = Image.objects.all()
   context = {'images':images, 'q':q}
   return render(request, 'pictures/search_results.html', context)


def addPage(request):
   form = ImageForm()
   context = {'form':form}
   return render(request, 'pictures/add_image.html', context)
  

  
  
