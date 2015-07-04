from django.forms import forms

class ImageUpload(forms.Form):
    image = forms.FileField
    #image = forms.ImageField()

