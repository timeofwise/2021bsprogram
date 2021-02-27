from django.urls import path
from .views import *

urlpatterns = [
    path('', ReportsView, name='reports_list'),
    path('<slug:client_slug>/', ReportsView, name='reports_by_client'),
]