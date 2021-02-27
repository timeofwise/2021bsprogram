from django.urls import path
from .views import *

urlpatterns = [
    path('', PartsListView, name='parts'),
    path('<slug:client_slug>/', PartsListView, name='parts_by_client'),
]