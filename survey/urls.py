from django.urls import path
from .views import *

#app_name = 'survey'
urlpatterns = [
    path('', AddSurvey.as_view(), name='survey_add'),
    path('result/', DisplaySurvey.as_view(), name='survey_list'),
    path('complete/', SurveyComplete, name='survey_complete'),
]