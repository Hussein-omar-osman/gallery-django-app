from unicodedata import name
from django.forms import ModelForm
from .models import Image 

class ImageForm(ModelForm):
  
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['location'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['category'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['description'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['picture'].widget.attrs.update({'class':"form-control" ,'type':"file", 'id':"formFile"})
  class Meta:
   model = Image
   fields = '__all__'
   