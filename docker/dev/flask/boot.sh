#!/bin/sh
flask db upgrade
exec flask run
