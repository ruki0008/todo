from apps.app import db
from apps.auth.forms import SingUpForm, LoginForm
from apps.crud.models import User
from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_login import login_user, logout_user

auth = Blueprint(
    'auth',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@auth.get('/signup')
@auth.post('/signup')
def signup():
    form = SingUpForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )

        if user.is_duplicate_email():
            flash('指定のメールアドレスは登録済みです')
            return redirect(url_for('auth.signup'))
        
        db.session.add(user)
        db.session.commit()
        login_user(user)

        next_ = request.args.get('next')
        if next_ is None or not next_.startswith('/'):
            next_ = url_for('todo.index')
        return redirect(next_)
    
    return render_template('auth/signup.html', form=form)

@auth.get('/login')
@auth.post('/login')
def login():
    form = LoginForm()
    print('form')
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('todo.index'))
        flash('メールアドレスかパスワードが不正です')
        return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)

@auth.get('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))