#!/bin/bash

# TODO: Check virtualenv existance

FRONTEND_DIR="server/frontend"
VENV="$VIRTUALENVWRAPPER_HOOK_DIR/acb/"

sudo apt-get install redis-server

"$VENV"/bin/pip3 install -r requirements.txt
"$VENV"/bin/python3 manage.py collectstatic

cd "$FRONTEND_DIR"

npm install
gulp rebuild

sudo service uwsgi restart

