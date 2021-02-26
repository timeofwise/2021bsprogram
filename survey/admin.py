from django.contrib import admin
from .models import Survey
# Register your models here.

# admin.site.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'name', 'q2_overall', 'q3_3_recommend_to_other', 'created']
    # raw_id_fields = ['author']
    list_filter = ['company']
    search_fields = ['company']
    ordering = ['-created']

admin.site.register(Survey,SurveyAdmin)