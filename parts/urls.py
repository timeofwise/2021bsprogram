from django.urls import path
from .views import *

urlpatterns = [
    path('', PartsListView, name='parts'),
]