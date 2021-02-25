from django.urls import path
from .views import *

#app_name = 'survey'
urlpatterns = [
    path('', AddSurvey.as_view(), name='survey_add'),
    path('result/', DisplaySurvey.as_view(), name='survey_result'),
    path('complete/', SurveyComplete, name='survey_complete'),
]