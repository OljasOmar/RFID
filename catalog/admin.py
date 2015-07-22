from django.contrib import admin
from .models import Locations, Authors, Main_table, Loaning_period, User_info, LoanedBook


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
    list_display = ('title', 'author', 'year_pb', 'location', 'rfid', 'image', 'loaning_period', 'id')
    search_fields = ['author__name', 'title', 'location__department']
admin.site.register(Main_table, Main_tableAdmin)


class Loaning_periodAdmin(admin.ModelAdmin):
    list_display = ('period', 'calendar_days', 'id')
admin.site.register(Loaning_period, Loaning_periodAdmin)


class User_infoAdmin(admin.ModelAdmin):
    #readonly_fields = ('image_tag')
    list_display = ('name', 'department', 'barcode_id', 'id' )
    search_fields = ['name', 'department', 'barcode_id']
admin.site.register(User_info, User_infoAdmin)

class LoanedBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')
    search_fields = ['user__name', 'book__title']

admin.site.register(LoanedBook, LoanedBookAdmin)
