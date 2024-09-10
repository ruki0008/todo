from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class TodoForm(FlaskForm):
    todo_name = StringField(
        '目標名',
        validators=[
            DataRequired('目標名は必須です。'),
            Length(1, 50, '50文字以内で入力してください。')
        ]
    )
    todo_pt = IntegerField(
        '目標pt'
    )
    todo_pt_result = IntegerField(
        '現在pt'
    )
    move_1 = StringField(
        '行動1',
        validators=[
            DataRequired('行動1は必須です。'),
            Length(1, 30, '30文字以内で入力してください。')
        ]
    )
    move_2 = StringField(
        '行動2',
        validators=[
            DataRequired('行動2は必須です。'),
            Length(1, 30, '30文字以内で入力してください。')
        ]
    )
    move_3 = StringField(
        '行動3',
        validators=[
            DataRequired('行動3は必須です。'),
            Length(1, 30, '30文字以内で入力してください。')
        ]
    )
    move_4 = StringField(
        '行動4',
        validators=[
            DataRequired('行動4は必須です。'),
            Length(1, 30, '30文字以内で入力してください。')
        ]
    )
    move_pt_1 = IntegerField(
        '行動pt1'
    )
    move_pt_2 = IntegerField(
        '行動pt2'
    )
    move_pt_3 = IntegerField(
        '行動pt3'
    )
    move_pt_4 = IntegerField(
        '行動pt4'
    )
    submit = SubmitField('目標を登録')