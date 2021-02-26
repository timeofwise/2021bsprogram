from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView, BookmarkPrintView, BookmarkListDef

urlpatterns = [
    path('list/', BookmarkListView.as_view(), name='list2'),
    path('', BookmarkListDef, name='list'),
    path('<slug:client_slug>/', BookmarkListDef, name='sort_by_client'),
    path('add/item/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
    path('print/<int:pk>/', BookmarkPrintView.as_view(), name='print'),
]