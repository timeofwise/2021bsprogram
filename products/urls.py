from django.urls import path
from .views import *

urlpatterns = [
    path('software/t-solution/', software_t_solution, name="t-solution"),
]