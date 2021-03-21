from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark, Client
from django.urls import reverse_lazy

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 9

def BookmarkListDef(request, client_slug=None):
    current_client = None
    clients = Client.objects.all()
    bookmarks = Bookmark.objects.filter(available_display=True)

    if client_slug:
        current_client = get_object_or_404(Client, slug=client_slug)
        bookmarks = bookmarks.filter(client=current_client)
    return render(request, 'bookmark/list.html', {'bookmarks':bookmarks, 'current_client' : current_client, 'clients':clients})

'''
def BookmarkListByClient(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)
    return render(request, 'shop/list.html', {
        'current_category' : current_category,
        'categories' : categories,
        'products' : products,
    })
'''

class BookmarkCreateView(CreateView):
    model = Bookmark

    success_url = reverse_lazy('list')
    template_name_suffix = '_create' #CreateView class template의  기본접미사(_form) 변경 : _form -> _create

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkPrintView(DetailView):
    model = Bookmark
    template_name_suffix = '_print'

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

