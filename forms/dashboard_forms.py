from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length, Regexp

class CreateStudentRecordForm(FlaskForm):
    """ Create New Entry for a Student Record """
    student_name = StringField(
        'Name',
        validators=[
            DataRequired(), 
            Length(min=2),
            Regexp(r'^[A-Za-z\s]+$', message="Name must contain only letters")  # Enforces letters and spaces only
        ]
    )
    subject = StringField(
        'Subject',
        validators=[DataRequired()]
    )
    marks = IntegerField(
        'Marks',
        validators=[
            DataRequired(),
            NumberRange(min=0, max=100, message="Marks must be a positive number between 0-100")
        ]
    )
    submit = SubmitField("Add Record")