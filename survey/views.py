from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Survey
from bookmark.models import Bookmark
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
        'q3_21_fi_smart_erp',
        'q3_22_fi_factory_automation',
        'q3_23_fi_remote_support',
        'q3_24_fi_systematical_training',
        'q3_25_fi_other',
        'q3_25_other',
        'q3_3_recommend_to_other',
        'manager_opinion',
        'policy_agreement',
    ]
    success_url = reverse_lazy('survey_complete')
    template_name_suffix = '_create' #CreateView class template의  기본접미사(_form) 변경 : _form -> _create

def SurveyComplete(request):
    return render(request, 'survey/survey_complete.html')


class DisplaySurvey(ListView):
    model = Survey