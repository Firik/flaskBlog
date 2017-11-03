##!/usr/bin/env bash
#source ~/.venv/flaskBlog/bin/activate
sudo systemctl start postgresql.service
export FLASK_APP=app.py
export APP_SETTINGS="config.DevelopmentConfig"
#export FLASK_DEBUG=1
#export DATABASE_URL="postgresql://flaskblog:123456@localhost/flask_blog"
#flask run