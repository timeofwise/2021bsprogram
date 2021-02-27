from django.contrib import admin
from .models import Bookmark, Machine, Client, Consumed
# Register your models here.

admin.site.register(Bookmark)
# admin.site.register(Client)
#admin.site.register(Machine)

# Register your models here.
from .models import *
"""
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'model_type', 'model_no', 'available_display', 'visibility', 'slug', 'created', 'updated']
    # raw_id_fields = ['author']
    list_editable = ['slug', 'visibility', 'available_display']
    list_filter = ['client', 'created', 'updated']
    search_fields = ['client', 'created', 'model_type']
    ordering = ['-updated', '-created']

admin.site.register(Bookmark,BookmarkAdmin)
"""
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'slug']
    list_editable = ['slug']

admin.site.register(Client,ClientAdmin)

class MachineAdmin(admin.ModelAdmin):
    list_display = ['id', 'model_type', 'part1']
    # raw_id_fields = ['author']

admin.site.register(Machine,MachineAdmin)

class ConsumedAdmin(admin.ModelAdmin):
    list_display = ['id', 'part_code', 'part_name', 'part_img', 'part_desc']
    # raw_id_fields = ['author']

admin.site.register(Consumed,ConsumedAdmin)