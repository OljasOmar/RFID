from django.contrib import admin
from .models import Locations, Authors, Main_table

# Register your models here.
admin.site.register(Locations)
admin.site.register(Authors)
admin.site.register(Main_table)
