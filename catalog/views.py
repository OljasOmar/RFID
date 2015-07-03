from catalog.forms import ImageUpload
from catalog.models import Main_table
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            m = Main_table.objects.get(pk=id)
            m.image = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')