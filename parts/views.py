from django.shortcuts import render, redirect
from django.views.generic.list import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from bookmark.models import Bookmark, Consumed, Machine
from django.urls import reverse_lazy

def PartsListView(request):
    # 보여줄 사진 데이터
    machines = Machine.objects.all()
    lists = Bookmark.objects.filter(available_display=True)
    parts = Consumed.objects.all()
    sm421 = 'SM421'
    sm411 = 'SM411'
    decan_f2 = 'DECAN F2'


    return render(request, 'parts/parts.html', {'lists' : lists, 'parts' : parts, 'machines' : machines, 'sm421' : sm421, 'sm411' : sm411})