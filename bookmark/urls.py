from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView, BookmarkPrintView, BookmarkListDef

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('list/', BookmarkListDef, name='list2'),
    #path('<slug:category_slug>/', product_in_category, name='product_in_category'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
    path('print/<int:pk>/', BookmarkPrintView.as_view(), name='print'),
]