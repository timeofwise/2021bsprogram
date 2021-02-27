from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from bookmark.models import Bookmark, Consumed, Machine, Client
from django.db.models import Sum
from django.urls import reverse_lazy

def ReportsView(request, client_slug=None):
    current_client = None
    clients = Client.objects.all()
    bookmarks = Bookmark.objects.filter(available_display=True)
    if client_slug:
        current_client = get_object_or_404(Client, slug=client_slug)
        bookmarks = bookmarks.filter(client=current_client)
    return render(request, 'reports/list.html', {'bookmarks':bookmarks, 'current_client' : current_client, 'clients':clients})