from flask import flash, redirect, render_template, url_for

from . import home
from forms import AdmitAnimalForm
from .. import db
from ..models import Animal

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="ZOO-APP")


@home.route('/add_animal', methods=['GET', 'POST'])
def add_animal():
    form = AdmitAnimalForm()
    if form.validate_on_submit():
        animal = Animal(name=form.name.data,
                        description=form.description.data)
        db.session.add(animal)
        db.session.commit()
        flash('You have successfully admitted an animal!')
        return redirect(url_for('home.homepage'))
    return render_template('home/add_animal.html', form=form, title='Add Animal')
