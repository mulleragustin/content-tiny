from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    ProyectoListView,
    ProyectoDetailView,
    CategoriaListView
)

urlpatterns = [
    # Blogs
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),

    # Proyectos
    path('proyectos/', ProyectoListView.as_view(), name='proyecto-list'),
    path('proyectos/<slug:slug>/',
         ProyectoDetailView.as_view(), name='proyecto-detail'),

    # Categorías
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
]
