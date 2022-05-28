from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
  name = models.CharField(max_length=200)
  def __str__(self):
      return self.name
     
class Category(models.Model):
  name = models.CharField(max_length=200)
  def __str__(self):
      return self.name
     
class Image(models.Model):
  name = models.CharField(max_length=200)
  location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  picture = CloudinaryField('picture')
  description = models.TextField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  class Meta:
   ordering = ['-created']
  def __str__(self):
      return self.name
