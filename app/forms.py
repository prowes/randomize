from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class EnterForm(FlaskForm):
    down_border = IntegerField('From', validators=[DataRequired()])
    up_border = IntegerField('To', validators=[DataRequired()])
    submit = SubmitField('Randomize')