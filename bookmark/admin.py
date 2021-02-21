from django.contrib import admin
from .models import Bookmark, Machine, Client
# Register your models here.

admin.site.register(Bookmark)
admin.site.register(Client)
admin.site.register(Machine)