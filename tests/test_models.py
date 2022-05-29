from django.test import TestCase
from pictures.models import Image, Location, Category


class TestModel(TestCase):
   def test_create_location(self):
    location = Location.objects.create(name='berlin')
    location.save()
    
    self.assertEqual(str(location), 'berlin')
    
   def test_create_Category(self):
    category = Category.objects.create(name='sports')
    category.save()
    
    self.assertEqual(str(category), 'sports')
    
   def test_create_Image(self):
    category = Category.objects.create(name='sports')
    category.save()
    location = Location.objects.create(name='berlin')
    location.save()
    image = Image.objects.create(name='banana', location=location, category=category, 
                                 picture='image/upload/v1653771990/zqwahiwjbgffmz0s8zmv.jpg',
                                 description='Its a banana', created='2022-05-28 12:14:36.94396+03')
    
    self.assertEqual(str(image), 'banana')