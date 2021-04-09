#!/usr/bin/env bash

echo "creating tables..."
flask db upgrade
echo "running app ..."
python3 -m flask run --host=0.0.0.0