from datetime import datetime
from apps.app import db

class UserTodo(db.Model):
    __tablename__ = 'user_todos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    todo_name = db.Column(db.String)
    todo_pt = db.Column(db.Integer)
    todo_pt_result = db.Column(db.Integer)
    move_1 = db.Column(db.String)
    move_2 = db.Column(db.String)
    move_3 = db.Column(db.String)
    move_4 = db.Column(db.String)
    move_pt_1 = db.Column(db.Integer)
    move_pt_2 = db.Column(db.Integer)
    move_pt_3 = db.Column(db.Integer)
    move_pt_4 = db.Column(db.Integer)
    todo_path = db.Column(db.String)
