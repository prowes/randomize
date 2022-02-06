from app import app
from app.forms import EnterForm
from random import randint
from flask import render_template


@app.route('/enter', methods=['GET', 'POST'])
def enter():
    form = EnterForm()
    if form.validate_on_submit():
        value = randint(form.down_border.data, form.up_border.data)
        return render_template('index.html', value=str(value))
    return render_template('enter.html', title='Enter numbers', form=form)