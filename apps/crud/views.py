from flask import Blueprint, render_template, redirect, url_for
from apps.app import db
from apps.crud.models import User
from apps.crud.forms import UserForm
from flask_login import login_required, current_user

crud = Blueprint(
    'crud',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@crud.get('/users')
@login_required
def users():
    if current_user.is_admin == False:
        return render_template('todo/index.html')
    users = User.query.all()
    return render_template('crud/index.html', users=users)

@crud.get('/users/<user_id>')
@crud.post('/users/<user_id>')
@login_required
def edit_user(user_id):
    if current_user.is_admin == False:
        return render_template('todo/index.html')
    form = UserForm()
    user = User.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('crud.users'))
    return render_template('crud/edit.html', user=user, form=form)

@crud.post('/users/<user_id>/delete')
@login_required
def delete_user(user_id):
    if current_user.is_admin == False:
        return render_template('todo/index.html')
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('crud.users'))