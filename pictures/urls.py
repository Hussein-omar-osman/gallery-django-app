from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('result/', views.searchPage, name='searchPage'),
    path('add-image/', views.addPage, name='addPage'),
]