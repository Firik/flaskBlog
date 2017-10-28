from flask import render_template, Blueprint

from models.Blog import Blog

index_page = Blueprint('index_page', __name__, template_folder='templates')


@index_page.route('/')
def index():
    blogs = dict(a='a', b='b')
    return render_template('index.html', blogs=blogs)
