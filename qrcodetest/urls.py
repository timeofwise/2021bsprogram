from django.urls import path
from .views import *

urlpatterns = [
    path('', getQRInfo, name='get_qr_info'),
    path('list/', QRListView.as_view(), name='list_qr_info'),
]