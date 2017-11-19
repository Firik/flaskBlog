from flask import render_template, Blueprint, request, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError

from models.Blog import Blog

index_page = Blueprint('index_page', __name__, template_folder='templates')


@index_page.route('/')
def index():
    return render_template('index.html', blogs=Blog.get_blogs())


@index_page.route('/blog/add/', methods=['GET'])
def add():
    return render_template('add_blog_form.html')


@index_page.route('/blog/save/', methods=['POST'])
def save_blog():
    url = '/'
    if request.method == 'POST':
        caption = request.form.get('caption')
        description = request.form.get('description')

        if not caption or not description:
            url = url_for('index_page.add')
            flash('Запись не сохранена')
            return redirect(url)

        blog_object = Blog(caption, description)

        try:
            blog_object.save()
        except IntegrityError:
            flash('Запись не сохранена')
            url = url_for('index_page.add')

    return redirect(url)


@index_page.route('/blog/<int:blog_id>/')
def show_blog(blog_id):
    blog_object = Blog.query.get(blog_id)
    return render_template('blog.html', blog=blog_object)
