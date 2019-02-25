#!/bin/sh
yarn install
pip install -e .
flask build -d
