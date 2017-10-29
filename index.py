from flask import render_template, Blueprint, request, redirect

from models.Blog import Blog
from app import db

index_page = Blueprint('index_page', __name__, template_folder='templates')


@index_page.route('/')
def index():
    blogs = Blog.query.with_entities(Blog.caption, Blog.description, Blog.dt_create)
    return render_template('index.html', blogs=blogs)


@index_page.route('/blog/save/', methods=['POST'])
def save_blog():
    if request.method == 'POST':
        blog = Blog(request.form.get('caption'), request.form.get('description'))
        db.session.add(blog)
        db.session.commit()

    return redirect('/')
