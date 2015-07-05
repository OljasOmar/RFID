from catalog.forms import ImageUpload
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from .models import Main_table, Locations, Authors

# Create your views here.
def post_list(request):
    books = Main_table.objects.filter().order_by('id')
    locations = Locations.objects.all()
    authors = Authors.objects.all()
    return render(request, 'catalog/post_list.html', {'books':books, 'loc':locations, 'authors': authors})

def upload_pic(request):
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            m = Main_table.objects.get(pk=id)
            m.image = form.cleaned_data['image']
            form.save()
            return HttpResponse('image upload success')
        return HttpResponseForbidden('allowed only via POST')

'''def post_list(request):
    main_table = Main_table.objects.filter().order_by('id')
    return render(request, 'catalog/post_list.html', {'main_table': main_table})
'''


