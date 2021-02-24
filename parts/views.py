from django.shortcuts import render, redirect
from django.views.generic.list import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from bookmark.models import Bookmark, Consumed
from django.urls import reverse_lazy

def PartsListView(request):
    # 보여줄 사진 데이터
    lists = Bookmark.objects.all()
    parts = Consumed.objects.all()


    return render(request, 'parts/parts.html', {'lists' : lists, 'parts' : parts})