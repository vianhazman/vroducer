#!/bin/bash
source .env

if [ "$ENVIRONMENT" == "Production" ];
then gunicorn --bind 0.0.0.0:8080 --workers=$WSGI_WORKERS --threads=$WSGI_THREADS wsgi:app
else python -m main
fi