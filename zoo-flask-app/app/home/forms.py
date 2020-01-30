from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Animal


class AdmitAnimalForm(FlaskForm):
    """
    Form for users to create new account
    """
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_animal(self, field):
        if Animal.query.filter_by(name=field.data).first():
            raise ValidationError('Animal has already been submitted.')

