from django.contrib import admin
from .models import Locations, Authors, Main_table


# Register your models here.
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ['name']

admin.site.register(Authors, AuthorsAdmin)

class LocationsAdmin(admin.ModelAdmin):
    list_display = ('department', 'shelve', 'bookCode', 'id')
    search_fields = ['department', 'shelve', 'bookCode']

admin.site.register(Locations, LocationsAdmin)

class Main_tableAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    list_display = ('title', 'author', 'year_pb', 'location', 'rfid', 'image', 'id')
    search_fields = ['author__name', 'title', 'location__department']

admin.site.register(Main_table, Main_tableAdmin)