from flask import render_template, Blueprint, request, redirect

from models.Blog import Blog

blog_page = Blueprint('index_page', __name__, template_folder='templates')


@blog_page.route('/')
def index():
    return render_template('index.html', blogs=Blog.get_blogs())


@blog_page.route('/blog/save/', methods=['POST'])
def save_blog():
    if request.method == 'POST':
        blog = Blog(request.form.get('caption'), request.form.get('description'))
        blog.save()

    return redirect('/')
