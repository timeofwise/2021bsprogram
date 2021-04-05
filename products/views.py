from django.shortcuts import render

# Create your views here.

def software_t_solution(request):
    template='softwares/t-solution.html'
    context={}
    return render(request, template, context)