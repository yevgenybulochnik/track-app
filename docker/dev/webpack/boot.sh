#!/bin/sh
yarn install
exec flask build -d
