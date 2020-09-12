from flask import render_template, request, Blueprint
from Main.models import Post
import flask_whooshalchemy
index = Blueprint('index',__name__)

@index.route('/')
@index.route('/home')
def home():
	page = request.args.get('page',1,type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=3)
	return render_template('home.html',posts = posts)

@index.route('/search')
def search():
	posts = Post.query.search(request.args.get('query')).all()
	return render_template('home.html',posts = posts)
