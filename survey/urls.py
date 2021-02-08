from django.urls import path
from .views import *

app_name = 'survey'
urlpatterns = [
    path('', AddSurvey, name='add'),
]