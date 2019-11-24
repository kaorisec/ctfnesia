from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    name = StringField('Nama doggy: ', validators=[DataRequired()])
    submit = SubmitField('GUK!')
