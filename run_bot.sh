#!/bin/bash

PYTHON="/usr/bin/python3"
DIR="venv"

$PYTHON -m venv $DIR
source $DIR/bin/activate

echo "************ Installing requirements... ************"

python -m pip install --upgrade pip

python -m pip install -r requirements.txt

python src/app.py
