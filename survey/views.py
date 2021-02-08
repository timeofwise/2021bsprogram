from django.shortcuts import render

# Create your views here.

def AddSurvey(request):
    return render(request, 'survey/add.html')