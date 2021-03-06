from flask import Flask
application = Flask(__name__)
application.config['SECRET_KEY']='some_random_secret'

from random import randint
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
import os

@application.route('/', methods=['GET', 'POST'])
def enter():
    form = EnterForm()
    if form.validate_on_submit():
        value = randint(form.down_border.data, form.up_border.data)
        return (f"Your number is {str(value)}, refresh the page for the new one!")
    return (f'<html><head><title>Random number generator</title></head><body><form action="" method="post" novalidate>{form.hidden_tag()}<p>{form.down_border.label}<br>{form.down_border(size=7)}</p><p>{form.up_border.label}<br>{ form.up_border(size=7)}<p>{form.submit()}</p></form></body></html>')


class EnterForm(FlaskForm):
    down_border = IntegerField('From', validators=[DataRequired()])
    up_border = IntegerField('To', validators=[DataRequired()])
    submit = SubmitField('Randomize')
