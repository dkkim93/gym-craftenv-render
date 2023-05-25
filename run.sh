#!/bin/bash

# load python virtualenv
virtualenv --python=/opt/homebrew/bin/python3.10 venv
source venv/bin/activate
pip3 install -r requirements.txt

# append python path
export PYTHONPATH=$PYTHONPATH:./sgminigrid/

# run main.py
python main.py
