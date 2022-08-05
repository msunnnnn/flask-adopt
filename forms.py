from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Forms for adopt pet."""


    name = StringField("Pet name:",
        validators= [InputRequired()])

    species = SelectField("Species:",
        choices= [('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
        validators= [InputRequired()])

    photo_url = StringField("Photo URL",
        validators=[URL(), Optional()])

    age = SelectField("Age:",
        choices= [('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'),
                  ('senior', 'Senior')],
        validators= [InputRequired()])

    notes = TextAreaField("Notes:",
        validators=[Optional()])

class EditPetForm(FlaskForm):
    """Forms for edit pet."""

    photo_url = StringField("Photo URL",
        validators=[URL(), Optional()])

    available = BooleanField("available")

    notes = TextAreaField("Notes:",
        validators=[Optional()])

