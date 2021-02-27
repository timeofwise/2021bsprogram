from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from bookmark.models import Bookmark, Consumed, Machine, Client
from django.db.models import Sum, Max
from django.urls import reverse_lazy

def ReportsView(request, client_slug=None):
    current_client = None
    clients = Client.objects.all()
    bookmarks = Bookmark.objects.filter(available_display=True)
    line_rowspan = [0]
    line_max={}
    if client_slug:
        current_client = get_object_or_404(Client, slug=client_slug)
        bookmarks = bookmarks.filter(client=current_client)

        # for making rowspan having same line
        line_max = bookmarks.aggregate(Max('line'))
        line_max['min'] = [6,7,8]
        line_max_int = int(line_max.get('line__max'))

        for i in range(line_max_int):
            row = bookmarks.filter(line=i+1)
            line_rowspan.append(len(row))

    return render(request, 'reports/list.html', {'bookmarks':bookmarks, 'current_client' : current_client, 'clients':clients, 'line_rowspan' : line_rowspan, 'line_max' : line_max})