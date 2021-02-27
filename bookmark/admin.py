from django.contrib import admin
from .models import Bookmark, Machine, Client, Consumed
# Register your models here.

# admin.site.register(Bookmark)
# admin.site.register(Client)
#admin.site.register(Machine)

# Register your models here.
from .models import *
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'model_type', 'model_no', 'line', 'order', 'available_display', 'visibility', 'slug', 'created', 'updated']
    # raw_id_fields = ['author']
    list_editable = ['slug', 'visibility', 'available_display', 'line', 'order']
    list_filter = ['client', 'created', 'updated']
    search_fields = ['client', 'created', 'model_type']
    ordering = ['-client', 'line', 'order']

admin.site.register(Bookmark,BookmarkAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'slug']
    list_editable = ['slug']

admin.site.register(Client,ClientAdmin)

class ReportItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'num', 'item']
    list_editable = ['num', 'item']

admin.site.register(Reportitem,ReportItemAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'item', 'mini_title', 'desc', 'img', 'target_goods', 'target_goods_price', 'target_goods_qty']
    list_editable = ['client', 'item', 'mini_title', 'desc', 'img']

admin.site.register(Report,ReportAdmin)

class MachineAdmin(admin.ModelAdmin):
    list_display = ['id', 'part1_qty', 'part2_qty', 'part3_qty', 'part4_qty', 'part5_qty', 'part6_qty', 'part7_qty']
    list_editable = ['part1_qty', 'part2_qty', 'part3_qty', 'part4_qty', 'part5_qty', 'part6_qty', 'part7_qty']
    # raw_id_fields = ['author']

admin.site.register(Machine,MachineAdmin)

class ConsumedAdmin(admin.ModelAdmin):
    list_display = ['id', 'part_code', 'part_name', 'part_img', 'part_desc']
    # raw_id_fields = ['author']

admin.site.register(Consumed,ConsumedAdmin)