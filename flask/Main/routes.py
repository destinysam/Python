import os
import secrets
from PIL import Image
from Main import app,bcrypt,db,app,mail
from flask import render_template,url_for,redirect,flash,request,abort
from Main.forms import RegisterForm,LoginForm,UpdateAccountForm,PostForm,RequestResetPassword,ResetPasswordForm
from Main.models import User,Post 
from flask_login import login_user,current_user,logout_user,login_required
from flask_mail import Message
@app.route('/')
@app.route('/home')
def home():
	page = request.args.get('page',1,type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=3)
	return render_template('home.html',posts = posts)

