from catalog.forms import ImageUpload
from django.core import serializers
from django.core.serializers import json
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from .models import Main_table, Locations, Authors, User_info

# Create your views here.
def post_list(request):
    books = Main_table.objects.filter().order_by('id')
    locations = Locations.objects.all()
    authors = Authors.objects.all()
    return render(request, 'catalog/post_list.html', {'books':books, 'loc':locations, 'authors': authors})

def book_info(request, rfidValue):
    try:
        book = Main_table.objects.get(rfid=rfidValue)
        return HttpResponse(serializers.serialize("json", [book]))
    except Main_table.DoesNotExist:
        return HttpResponse("Error")

def user_info(request, barcodeValue):
    try:
        user = User_info.objects.get(barcode_id=barcodeValue)
        to_json = {
            "success": "true",
            "barcode": user.barcode_id,
            "name": user.name,
            "department": user.department
        }
        return JsonResponse(to_json)
        #return  HttpResponse(serializers.serialize("json", [user]))
    except User_info.DoesNotExist:
        return  HttpResponse("Error, does not exist")


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            m = Main_table.objects.get(pk=id)
            m.image = form.cleaned_data['image']
            form.save()
            return HttpResponse('image upload success')
        return HttpResponseForbidden('allowed only via POST')

#user photo
'''def upload_userPhoto(request):
    if request.method =='POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            p = User_info.objects.get(pk=id)
            p.user_photo=form.cleaned_data['user_photo']
            form.save()
            return HttpResponse('photo uploaded')
        return HttpResponseForbidden('Error')'''