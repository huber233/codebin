from django.urls import path
from . import views

urlpatterns = [
    path('', views.snippet_list, name='snippet-list'),
    path('search/', views.snippet_search, name='snippet-search'),
    path('new/', views.snippet_create, name='snippet-create'),
    path('<slug:slug>/', views.snippet_detail, name='snippet-detail'),
    path('<slug:slug>/edit/', views.snippet_update, name='snippet-update'),
    path('<slug:slug>/delete/', views.snippet_delete, name='snippet-delete'),
    path('language/<slug:slug>/', views.language_snippets, name='language-snippets'),
]