#!/bin/bash

# load python virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt

# run main.py
python main.py
