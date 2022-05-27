from django.shortcuts import redirect, render


# Create your views here.
def homePage(request):
   context = {}
   return render(request, 'pictures/home.html', context)
  
def homePage2(request):
   context = {}
   return render(request, 'pictures/home2.html', context)
  
  
