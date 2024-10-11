from flask import Blueprint, render_template, redirect, url_for, current_app, send_from_directory, request,jsonify, flash
from flask_login import login_required, current_user
from apps.todo.models import UserTodo
from apps.todo.forms import TodoCreateForm, TodoEditForm
from apps.crud.models import User
import string
import random
from apps.app import db
import datetime

todo = Blueprint(
    'todo',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@todo.get('/')
@login_required
def index():
    return render_template('todo/index.html')

@todo.get('/lottie/<path:filename>')
@login_required
def lottie_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

@todo.get('/create')
@todo.post('/create')
@login_required
def create_todo():
    todos = UserTodo.query.filter_by(user_id=current_user.id).all()
    user = User.query.filter_by(id=current_user.id).first()
    user_path = user.user_path
    if todos == None:
        len_todo = 0
    len_todo = len(todos)
    print(len_todo)
    if len_todo >= 2 and user.is_admin == False:
        flash('目標は２つまでしか登録できません')
        return redirect(url_for('todo.todos', user_path=user_path))
    form = TodoCreateForm()
    print('form')
    if form.validate_on_submit():
        user_id=current_user.id
        todo_name=form.todo_name.data
        todo_pt=form.todo_pt.data
        todo_pt_result=form.todo_pt.data
        move_1=form.move_1.data
        move_2=form.move_2.data
        move_3=form.move_3.data
        move_4=form.move_4.data
        move_pt_1=form.move_pt_1.data
        move_pt_2=form.move_pt_2.data
        move_pt_3=form.move_pt_3.data
        move_pt_4=form.move_pt_4.data
        target_day=form.target_day.data
        todo_path = generate_random_string()
        while True:
            if not UserTodo.query.filter_by(todo_path=todo_path).first():
                break
            todo_path = generate_random_string()
        
        todo = UserTodo(user_id=user_id, todo_name=todo_name, todo_pt=todo_pt, todo_pt_result=todo_pt_result, move_1=move_1, move_2=move_2, move_3=move_3, move_4=move_4, move_pt_1=move_pt_1, move_pt_2=move_pt_2, move_pt_3=move_pt_3, move_pt_4=move_pt_4, target_day=target_day, todo_path=todo_path)
        db.session.add(todo)
        db.session.commit()
        user = User.query.filter_by(id=current_user.id).first()
        user_path = user.user_path
        print('redirect')
        return redirect(url_for('todo.todos', user_path=user_path))
    return render_template('todo/create.html', form=form)

@todo.get('/<user_path>/<todo_path>/edit')
@todo.post('/<user_path>/<todo_path>/edit')
@login_required
def edit_todo(todo_path, user_path):
    form = TodoEditForm()
    todo = UserTodo.query.filter_by(todo_path=todo_path).first()
    if todo.user_id != current_user.id:
        return redirect(url_for('todo.todos', user_path=current_user.user_path))
    if form.validate_on_submit():
        todo.todo_name=form.todo_name.data
        todo.todo_pt=form.todo_pt.data
        todo.todo_pt_result=form.todo_pt_result.data
        todo.move_1=form.move_1.data
        todo.move_2=form.move_2.data
        todo.move_3=form.move_3.data
        todo.move_4=form.move_4.data
        todo.move_pt_1=form.move_pt_1.data
        todo.move_pt_2=form.move_pt_2.data
        todo.move_pt_3=form.move_pt_3.data
        todo.move_pt_4=form.move_pt_4.data
        todo.target_day=form.target_day.data

        user = User.query.filter_by(id=current_user.id).first()
        user_path = user.user_path

        if todo.todo_pt_result > todo.todo_pt:
            flash('現在ptは目標pt以下で入力してください')
            return redirect(url_for('todo.edit_todo', todo_path=todo.todo_path, user_path=user_path))
        
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.todos', user_path=user_path))
    return render_template('todo/edit.html', todo=todo, form=form)

@todo.post('/<user_path>/<todo_path>/delete')
@login_required
def delete_todo(todo_path, user_path):
    todo = UserTodo.query.filter_by(todo_path=todo_path).first()
    if todo.user_id != current_user.id:
        return redirect(url_for('todo.todos', user_path=current_user.user_path))
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.todos', user_path=user_path))

@todo.get('/<user_path>/todos')
@todo.post('/<user_path>/todos')
@login_required
def todos(user_path):
    todos = UserTodo.query.filter_by(user_id=current_user.id).all()
    return render_template('todo/todos.html', todos=todos)

@todo.get('/<user_path>/<todo_path>/start')
@todo.post('/<user_path>/<todo_path>/start')
@login_required
def start_todo(todo_path, user_path):
    todo = UserTodo.query.filter_by(todo_path=todo_path).first()
    if todo.target_day:
        days_left = (todo.target_day - datetime.date.today()).days
    else:
        days_left = None
    print(todo.todo_name)
    if str(todo.user_id) != str(current_user.id):
        return redirect(url_for('todo.todos', user_path=current_user.user_path))
    if int(todo.todo_pt_result) <= 0:
        result_p = 0
    else:
        result_p = (todo.todo_pt_result / todo.todo_pt) * 100
    filename1 = 'AttAnim2'
    filename2 = 'AttAnim'
    filename3 = 'AttAnim3'
    filenameF = 'FinishAnim'
    return render_template('todo/start.html', todo=todo, result_p=result_p, filename1=filename1, filename2=filename2, filename3=filename3, filenameF=filenameF, days_left=days_left)

@todo.get('/update_pt')
@todo.post('/update_pt')
def update_pt():
    data = request.get_json()  # JSONデータを取得
    if not data:
        return jsonify({'message': 'データが受け取れませんでした'}), 400
    todo_id = data.get('id')  # todo_idを取得
    new_pt = int(data.get('pt'))
    
    # データベースから該当のTodoを取得
    todo = UserTodo.query.filter_by(id=todo_id).first()
    
    if todo:
        todo.todo_pt_result = new_pt  # ptを新しい値に更新
        db.session.add(todo)
        db.session.commit()  # データベースに保存
        return jsonify({'message': f"現在ポイントを {new_pt} に更新しました。"})
    else:
        return jsonify({'message': "Todoが見つかりませんでした。"}), 404
    
def generate_random_string(length=15):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string