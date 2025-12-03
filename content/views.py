from django.http import JsonResponse
from django.views import View
from django.db import connection
from .models import Blog, Proyecto, Categoria


class HealthCheckView(View):
    """Endpoint para verificar el estado del servidor"""

    def get(self, request):
        # Verificar conexión a la base de datos
        db_status = 'ok'
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1')
        except Exception as e:
            db_status = f'error: {str(e)}'

        return JsonResponse({
            'status': 'ok' if db_status == 'ok' else 'degraded',
            'database': db_status,
        })


class BlogListView(View):
    """API endpoint para listar blogs"""

    def get(self, request):
        blogs = Blog.objects.filter(publicado=True).select_related('categoria')

        # Filtros opcionales
        categoria_slug = request.GET.get('categoria')
        if categoria_slug:
            blogs = blogs.filter(categoria__slug=categoria_slug)

        data = []
        for blog in blogs:
            data.append({
                'id': blog.id,
                'titulo': blog.titulo,
                'slug': blog.slug,
                'descripcion': blog.descripcion,
                'imagen_principal': request.build_absolute_uri(blog.imagen_principal.url) if blog.imagen_principal else None,
                'categoria': {
                    'nombre': blog.categoria.nombre,
                    'slug': blog.categoria.slug
                } if blog.categoria else None,
                'fecha': blog.fecha.isoformat(),
            })

        return JsonResponse({'blogs': data}, safe=False)


class BlogDetailView(View):
    """API endpoint para obtener un blog por slug"""

    def get(self, request, slug):
        try:
            blog = Blog.objects.select_related(
                'categoria').get(slug=slug, publicado=True)
            data = {
                'id': blog.id,
                'titulo': blog.titulo,
                'slug': blog.slug,
                'descripcion': blog.descripcion,
                'imagen_principal': request.build_absolute_uri(blog.imagen_principal.url) if blog.imagen_principal else None,
                'categoria': {
                    'nombre': blog.categoria.nombre,
                    'slug': blog.categoria.slug
                } if blog.categoria else None,
                'fecha': blog.fecha.isoformat(),
            }
            return JsonResponse(data)
        except Blog.DoesNotExist:
            return JsonResponse({'error': 'Blog no encontrado'}, status=404)


class ProyectoListView(View):
    """API endpoint para listar proyectos"""

    def get(self, request):
        proyectos = Proyecto.objects.filter(
            publicado=True).select_related('categoria')

        # Filtros opcionales
        categoria_slug = request.GET.get('categoria')
        if categoria_slug:
            proyectos = proyectos.filter(categoria__slug=categoria_slug)

        data = []
        for proyecto in proyectos:
            data.append({
                'id': proyecto.id,
                'titulo': proyecto.titulo,
                'slug': proyecto.slug,
                'descripcion': proyecto.descripcion,
                'imagen_principal': request.build_absolute_uri(proyecto.imagen_principal.url) if proyecto.imagen_principal else None,
                'categoria': {
                    'nombre': proyecto.categoria.nombre,
                    'slug': proyecto.categoria.slug
                } if proyecto.categoria else None,
                'fecha': proyecto.fecha.isoformat(),
            })

        return JsonResponse({'proyectos': data}, safe=False)


class ProyectoDetailView(View):
    """API endpoint para obtener un proyecto por slug"""

    def get(self, request, slug):
        try:
            proyecto = Proyecto.objects.select_related(
                'categoria').get(slug=slug, publicado=True)
            data = {
                'id': proyecto.id,
                'titulo': proyecto.titulo,
                'slug': proyecto.slug,
                'descripcion': proyecto.descripcion,
                'imagen_principal': request.build_absolute_uri(proyecto.imagen_principal.url) if proyecto.imagen_principal else None,
                'categoria': {
                    'nombre': proyecto.categoria.nombre,
                    'slug': proyecto.categoria.slug
                } if proyecto.categoria else None,
                'fecha': proyecto.fecha.isoformat(),
            }
            return JsonResponse(data)
        except Proyecto.DoesNotExist:
            return JsonResponse({'error': 'Proyecto no encontrado'}, status=404)


class CategoriaListView(View):
    """API endpoint para listar categorías"""

    def get(self, request):
        categorias = Categoria.objects.all()
        data = [{'nombre': cat.nombre, 'slug': cat.slug} for cat in categorias]
        return JsonResponse({'categorias': data}, safe=False)
