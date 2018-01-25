from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'research/', views.research, name='research'),
    path(r'authors/', views.authors, name='authors'),
    path(r'about/', views.about, name='about'),
    path(r'editorial/', views.editorial, name='editorial'),
]
