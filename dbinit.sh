#!/bin/bash
set -e

until nc -z postgres 5432; do
    echo "$(date) - waiting for postgres..."
    sleep 1
done

sentry upgrade --noinput

python /usr/src/sentry/users.py
