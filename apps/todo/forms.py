from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class TodoCreateForm(FlaskForm):
    todo_name = StringField(
        '目標名',
        validators=[
            DataRequired('目標名は必須です。'),
            Length(1, 50, '50文字以内で入力してください。')
        ]
    )
    todo_pt = IntegerField(
        '目標pt',
        validators=[
            DataRequired('目標ptは必須です。'),
            NumberRange(min=1, max=10000, message=('1以上10000以下で入力してください'))
        ]
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
        '行動pt1',
        validators=[
            DataRequired('行動pt1は必須です。'),
            NumberRange(min=1, max=10000, message=('1以上10000以下で入力してください'))
        ]
    )
    move_pt_2 = IntegerField(
        '行動pt2',
        validators=[
            DataRequired('行動pt2は必須です。'),
            NumberRange(min=1, max=10000, message=('1以上10000以下で入力してください'))
        ]
    )
    move_pt_3 = IntegerField(
        '行動pt3',
        validators=[
            DataRequired('行動pt3は必須です。'),
            NumberRange(min=1, max=10000, message=('1以上10000以下で入力してください'))
        ]
    )
    move_pt_4 = IntegerField(
        '行動pt4',
        validators=[
            DataRequired('行動pt4は必須です。'),
            NumberRange(min=1, max=10000, message=('1以上10000以下で入力してください'))
        ]
    )
    submit = SubmitField('目標を登録')

class TodoEditForm(FlaskForm):
    todo_name = StringField(
        '目標名',
        validators=[
            DataRequired('目標名は必須です。'),
            Length(1, 50, '50文字以内で入力してください。')
        ]
    )
    todo_pt = IntegerField(
        '目標pt',
        validators=[
            DataRequired('目標ptは必須です。'),
            NumberRange(min=1, max=10000, message=('1以上10000以下で入力してください'))
        ]
    )
    todo_pt_result = IntegerField(
        '現在pt',
        validators=[
            DataRequired('現在ptは必須です。'),
            NumberRange(min=1, max=10000, message=('1以上10000以下で入力してください'))
        ]
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
        '行動pt1',
        validators=[
            DataRequired('行動pt1は必須です。'),
            NumberRange(min=1, max=10000, message=('1以上10000以下で入力してください'))
        ]
    )
    move_pt_2 = IntegerField(
        '行動pt2',
        validators=[
            DataRequired('行動pt2は必須です。'),
            NumberRange(min=1, max=10000, message=('1以上10000以下で入力してください'))
        ]
    )
    move_pt_3 = IntegerField(
        '行動pt3',
        validators=[
            DataRequired('行動pt3は必須です。'),
            NumberRange(min=1, max=10000, message=('1以上10000以下で入力してください'))
        ]
    )
    move_pt_4 = IntegerField(
        '行動pt4',
        validators=[
            DataRequired('行動pt4は必須です。'),
            NumberRange(min=1, max=10000, message=('1以上10000以下で入力してください'))
        ]
    )
    submit = SubmitField('目標を更新')