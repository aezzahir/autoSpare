#!/usr/bin/python3
""" forms Module for our project """
from models.user import User
from models import storage
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        storage.reload()
        session = storage.get_session()
        user = session.query(User).filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("username already exists! please try another username")
        
    def validate_email(self, email_to_check):
        storage.reload()
        session = storage.get_session()
        user = session.query(User).filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError("email already exists! please try another email")
        
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Adress:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Acount')


class LoginForm(FlaskForm):        
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')