from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Survey
from django.urls import reverse_lazy

# Create your views here.

class AddSurvey(CreateView):
#    return render(request, 'survey/add.html')

    model = Survey
    fields = [
        'name',
        'company',
        'mobile',
        'email',
        'position',
        'position_other',
        'q2_overall',
        'q2_sw',
        'q2_head_anc',
        'q2_xy',
        'q2_conveyor',
        'q2_feederbase',
        'q2_illumination',
        'q2_air',
        'q2_trust',
        'q2_trust_other',
        'q2_after_service',
        'q2_after_service_other',
        'q3_1_main_concern',
        'q3_2_1_future_interest_smart_erp',
        'q3_2_2_future_interest_factory_automation',
        'q3_2_3_future_interest_remote_support',
        'q3_2_4_future_interest_systematical_training',
        'q3_2_5_future_interest_other',
        'q3_2_5_other',
    ]
    success_url = reverse_lazy('survey_complete')
    template_name_suffix = '_create' #CreateView class template의  기본접미사(_form) 변경 : _form -> _create

def SurveyComplete(request):
    return render(request, 'survey/survey_complete.html')