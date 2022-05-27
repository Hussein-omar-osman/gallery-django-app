from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('home2', views.homePage2, name='homePage2'),
]