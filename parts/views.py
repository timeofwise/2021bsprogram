from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from bookmark.models import Bookmark, Consumed, Machine, Client
from django.urls import reverse_lazy

def PartsListView(request, client_slug=None):
    current_client = None
    clients = Client.objects.all()
    machines = Machine.objects.all()
    # lists = Bookmark.objects.all()
    lists = Bookmark.objects.filter(available_display=True)
    parts = Consumed.objects.all()

    if client_slug:
        current_client = get_object_or_404(Client, slug=client_slug)
        lists = lists.filter(client=current_client)


    return render(request, 'parts/parts.html', {'lists' : lists, 'parts' : parts, 'machines' : machines, 'clients' : clients, 'current_client' : current_client})