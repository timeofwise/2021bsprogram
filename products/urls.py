from django.urls import path
from .views import *

urlpatterns = [
    path('t-solution/softwares/', software_t_solution, name="t-solution"),
]