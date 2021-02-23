from django.contrib import admin
from .models import Bookmark, Machine, Client
# Register your models here.

# admin.site.register(Bookmark)
admin.site.register(Client)
admin.site.register(Machine)

# Register your models here.
from .models import *
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'created', 'updated']
    # raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'client']
    search_fields = ['client', 'created', 'model_type']
    ordering = ['-updated', '-created']

admin.site.register(Bookmark,BookmarkAdmin)