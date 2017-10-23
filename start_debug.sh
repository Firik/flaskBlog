#!/usr/bin/env bash
source ~/.venv/flaskBlog/bin/activate
export FLASK_APP=index.py
export FLASK_DEBUG=1
flask run