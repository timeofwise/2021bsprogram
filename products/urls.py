from django.urls import path
from .views import *

urlpatterns = [
    path('softwares/t-solution/', software_t_solution, name="t-solution"),
]