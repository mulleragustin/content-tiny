from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre


class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField(help_text='Contenido HTML del blog')
    imagen_principal = models.ImageField(upload_to='blogs/')
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        related_name='blogs'
    )
    fecha = models.DateTimeField(default=timezone.now)
    publicado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField(help_text='Contenido HTML del proyecto')
    imagen_principal = models.ImageField(upload_to='proyectos/')
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        related_name='proyectos'
    )
    fecha = models.DateTimeField(default=timezone.now)
    publicado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo
