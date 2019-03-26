#!/bin/sh

echo "Esperando a postgres"

while ! nc -z users-db 5432; do
    seleep 0.1
done

echo "postgres a iniciado"

python manage.py run -h 0.0.0.0