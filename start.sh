#!/bin/bash

gunicorn -k gevent -w 4 -b 0.0.0.0:9000 sentry.wsgi:application
