from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .forms import *
# Create your views here.

def getQRInfo(request):
    template = 'qrcodetest/get_qr_info.html'
    context ={}

    if request.method == "POST":
        qr_form = GetQRForm(request.POST)
        if qr_form.is_valid():
            get_qr = qr_form.save(commit=False)
            get_qr.save()
            #return render(request, 'books/blog.html', {'form': article, 'rand':rand})
            return render(request, 'qrcodetest/get_qr_info_complete.html', {'get_qr':get_qr})
    else:
        qr_form = GetQRForm()
    return render(request, template, {'form':qr_form})

class QRListView(ListView):
    model = qr_info