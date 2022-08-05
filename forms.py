from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email


class AddPetForm(FlaskForm):
    """Forms for adopt app."""


    name = StringField("Pet name:",
        validators= [InputRequired()])

    species = StringField("Species",
        validators= [InputRequired()])

    photo_url = StringField("Photo URL",
        validators=[Optional()])

    age = SelectField("Age:",
        choices= [('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'),
                  ('senior', 'Senior')],
        validators= [InputRequired()])
        
    notes = TextAreaField("Notes:",
        validators=[Optional()])



