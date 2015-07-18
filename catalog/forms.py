from django.forms import forms

class ImageUpload(forms.Form):
    image = forms.FileField

    #imageFiled check
    #user_photo = forms.FileField


