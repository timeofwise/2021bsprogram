from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = [
        'client',
        'model_type',
        'model_no',
        'inspector',
    ]
    success_url = reverse_lazy('list')
    template_name_suffix = '_create' #CreateView class template의  기본접미사(_form) 변경 : _form -> _create

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = [
        'model_no',
        'confirm_bs',
        'confirm_news',
        'col1',
        'col1_txt',
        'col2',
        'col2_txt',
        'col3',
        'col3_txt',
        'col4',
        'col4_txt',
        'col5',
        'col5_txt',
        'col6',
        'col6_txt',
        'col7',
        'col7_txt',
        'col8',
        'col8_txt',
        'col9',
        'col9_txt',
        'col10',
        'col10_txt',
        'col11',
        'col11_txt',
        'col12',
        'col12_txt',
        'col13',
        'col13_txt',
        'col14',
        'col14_txt',
        'col15',
        'col15_txt',
        'col16',
        'col16_txt',
        'col17',
        'col17_txt',
        'col18',
        'col18_txt',
        'col19',
        'col19_txt',
        'col20',
        'col20_txt',
        'col21',
        'col21_txt',
        'col22',
        'col22_txt',
        'col23',
        'col23_txt',
        'col24',
        'col24_txt',
        'col25',
        'col25_txt',
        'col26',
        'col26_txt',
        'col27',
        'col27_txt',
        'col28',
        'col28_txt',
        'col29',
        'col29_txt',
        'inspector',
        'bs_opinion',
        'manager_opinion',
    ]
    template_name_suffix = '_update'

    def form_valid(self, form):
        form.instance.manager_id = self.request.user.id
        if form.is_valid:
            form.instance.save()
            return redirect('/bookmark')
        else:
            return self.render_to_response({'form' : form})


#class BookmarkConfirmView(UpdateView):
#    model = Bookmark
#    fields = ['']

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

