#!/bin/sh
flask db upgrade
exec gunicorn -w 4 -b :5000 --access-logfile - --error-logfile - flask-base:app
