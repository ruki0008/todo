from flask import Blueprint, render_template, redirect, url_for, current_app, send_from_directory, request,jsonify
from flask_login import login_required, current_user
from apps.todo.models import UserTodo
from apps.todo.forms import TodoForm
from apps.app import db

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
    form = TodoForm()
    if form.validate_on_submit():
        todo = UserTodo(
            user_id=current_user.id,
            todo_name=form.todo_name.data,
            todo_pt=form.todo_pt.data,
            todo_pt_result=form.todo_pt.data,
            move_1=form.move_1.data,
            move_2=form.move_2.data,
            move_3=form.move_3.data,
            move_4=form.move_4.data,
            move_pt_1=form.move_pt_1.data,
            move_pt_2=form.move_pt_2.data,
            move_pt_3=form.move_pt_3.data,
            move_pt_4=form.move_pt_4.data
        )
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.todos'))
    return render_template('todo/create.html', form=form)

@todo.get('/<todo_id>/edit')
@todo.post('/<todo_id>/edit')
@login_required
def edit_todo(todo_id):
    form = TodoForm()
    todo = UserTodo.query.filter_by(id=todo_id).first()
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
        
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.todos'))
    return render_template('todo/edit.html', todo=todo, form=form)

@todo.post('/todo/<todo_id>/delete')
def delete_todo(todo_id):
    todo = UserTodo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.todos'))

@todo.get('/todos')
@todo.post('/todos')
@login_required
def todos():
    todos = UserTodo.query.filter_by(user_id=current_user.id).all()
    return render_template('todo/todos.html', todos=todos)

@todo.get('/<todo_id>/start')
@todo.post('/<todo_id>/start')
def start_todo(todo_id):
    todo = UserTodo.query.filter_by(id=todo_id).first()
    if int(todo.todo_pt_result) <= 0:
        result_p = 0
    else:
        result_p = (todo.todo_pt_result / todo.todo_pt) * 100
    filename1 = 'AttAnim2'
    filename2 = 'AttAnim'
    filenameF = 'FinishAnim'
    return render_template('todo/start.html', todo=todo, result_p=result_p, filename1=filename1, filename2=filename2, filenameF=filenameF)

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
        return jsonify({'message': f"Todo ID {todo_id} のポイントを {new_pt} に更新しました。"})
    else:
        return jsonify({'message': "Todoが見つかりませんでした。"}), 404