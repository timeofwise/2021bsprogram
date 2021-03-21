from django.contrib import admin
from .models import qr_info
# Register your models here.

# admin.site.register(Survey)
class QRAdmin(admin.ModelAdmin):
    list_display = ['id', 'model_name', 'model_no', 'created']

admin.site.register(qr_info,QRAdmin)