#!/bin/bash
# alias.sh

shopt -s expand_aliases

alias gulp='gulp --cwd server/frontend'
alias python3='$VIRTUALENVWRAPPER_HOOK_DIR/acb/bin/python3'

gulp rebuild
gulp watch &
python3 manage.py runserver
