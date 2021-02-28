from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from bookmark.models import *
from django.db.models import Sum, Max
from django.urls import reverse_lazy

def ReportsView(request, client_slug=None):
    current_client = None
    clients = Client.objects.all()
    bookmarks = Bookmark.objects.filter(available_display=True)
    reports = Report.objects.all()
    product = None
    bs_issue = None
    voc = None
    interested = None
    etc = None

    if client_slug:
        current_client = get_object_or_404(Client, slug=client_slug)
        bookmarks = bookmarks.filter(client=current_client)
        reports = reports.filter(client=current_client)
        product = reports.filter(item_id=6) #6-real, 5-test
        bs_issue = reports.filter(item_id=2) #2-real, 1-test
        voc = reports.filter(item_id=3)
        interested = reports.filter(item_id=4)
        etc = reports.filter(item_id=5)






    return render(request, 'reports/list.html', {
        'bookmarks':bookmarks,
        'current_client' : current_client,
        'clients':clients,
        'reports' : reports,
        'product' : product,
        'bs_issue' : bs_issue,
        'voc' : voc,
        'interested' : interested,
        'etc' : etc,
    })