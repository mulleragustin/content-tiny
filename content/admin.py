from django.contrib import admin
from django.db import models
from .models import Categoria, Blog, Proyecto


class HTMLEditorWidget(admin.widgets.AdminTextareaWidget):
    """Widget personalizado para el editor HTML"""
    class Media:
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-lite.min.css',)
        }
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-lite.min.js',
        )

    def __init__(self, attrs=None):
        default_attrs = {'class': 'summernote-editor', 'rows': 20, 'cols': 80}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha', 'publicado', 'created_at')
    list_filter = ('publicado', 'categoria', 'fecha')
    search_fields = ('titulo', 'descripcion')
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)

    fieldsets = (
        (None, {
            'fields': ('titulo', 'slug', 'imagen_principal', 'categoria')
        }),
        ('Contenido', {
            'fields': ('descripcion',),
            'classes': ('wide',)
        }),
        ('Publicación', {
            'fields': ('fecha', 'publicado')
        }),
    )

    class Media:
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-lite.min.css',)
        }
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-lite.min.js',
            'content/js/summernote-init.js',
        )


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha', 'publicado', 'created_at')
    list_filter = ('publicado', 'categoria', 'fecha')
    search_fields = ('titulo', 'descripcion')
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)

    fieldsets = (
        (None, {
            'fields': ('titulo', 'slug', 'imagen_principal', 'categoria')
        }),
        ('Contenido', {
            'fields': ('descripcion',),
            'classes': ('wide',)
        }),
        ('Publicación', {
            'fields': ('fecha', 'publicado')
        }),
    )

    class Media:
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-lite.min.css',)
        }
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-lite.min.js',
            'content/js/summernote-init.js',
        )
