#!/bin/sh
sleep 5 # waiting while postgres is being started
celery -A timeless.sync.celery worker
exec "$@"
