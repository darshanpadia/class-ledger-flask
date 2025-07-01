from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, IntegerField

from wtforms.validators import DataRequired, NumberRange, Length, Regexp

class LoginForm(FlaskForm):
    """"Form for teacher login with CSRF protection."""
    teacher_username = StringField('Username', validators=[DataRequired()])
    teacher_password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')