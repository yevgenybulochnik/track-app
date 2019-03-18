#!/bin/sh
yarn install
pip install -e .
exec flask build -d
