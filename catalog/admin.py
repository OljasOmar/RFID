from django.contrib import admin
from .models import Locations, Authors, Main_table

# Register your models here.
admin.site.register(Locations)
admin.site.register(Authors)


class Main_tableAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)

admin.site.register(Main_table, Main_tableAdmin)