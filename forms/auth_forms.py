# Import base form class from Flask-WTF
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, IntegerField

from wtforms.validators import DataRequired, NumberRange, Length, Regexp

# ---------------------------------------------
# LoginForm: Used to handle teacher login input
# Includes CSRF protection automatically via FlaskForm
# ---------------------------------------------
class LoginForm(FlaskForm):
    teacher_username = StringField('Username', validators=[DataRequired()])
    teacher_password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')