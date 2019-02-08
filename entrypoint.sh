#!/bin/sh
sleep 5 # waiting while postgres is being started
exec "$@"
