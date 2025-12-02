#!/bin/bash
set -e

# Esperar a la base de datos si está configurada
if [ -n "$DATABASE_URL" ]; then
    echo "Esperando a la base de datos..."
    sleep 5
fi

# Ejecutar migraciones
echo "Aplicando migraciones..."
python manage.py migrate --noinput

# Crear superusuario si las variables están definidas
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
    echo "Creando superusuario..."
    python manage.py createsuperuser --noinput || true
fi

# Iniciar Gunicorn
echo "Iniciando servidor..."
exec gunicorn content_manager.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --threads 4 \
    --timeout 120
