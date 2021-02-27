from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from bookmark.models import Bookmark, Consumed, Machine, Client
from django.db.models import Sum
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

    sum1 = 0
    for i in range(len(lists)):
        sum1 += int(lists[i].model_type.part1_qty)

    sum2 = 0
    for i in range(len(lists)):
        sum2 += int(lists[i].model_type.part2_qty)

    sum3 = 0
    for i in range(len(lists)):
        sum3 += int(lists[i].model_type.part3_qty)

    sum4 = 0
    for i in range(len(lists)):
        sum4 += int(lists[i].model_type.part4_qty)

    sum5 = 0
    for i in range(len(lists)):
        sum5 += int(lists[i].model_type.part5_qty)

    sum6 = 0
    for i in range(len(lists)):
        sum6 += int(lists[i].model_type.part6_qty)

    sum7 = 0
    for i in range(len(lists)):
        sum7 += int(lists[i].model_type.part7_qty)

    return render(request, 'parts/parts.html', {
        'lists' : lists,
        'parts' : parts,
        'machines' : machines,
        'clients' : clients,
        'current_client' : current_client,
        'sum1': sum1,
        'sum2': sum2,
        'sum3': sum3,
        'sum4': sum4,
        'sum5': sum5,
        'sum6': sum6,
        'sum7': sum7
    })