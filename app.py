"""Flask app for adopt app."""

from flask import Flask, redirect, render_template, request, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def load_root_page():
    """Redirect to list of pets."""
    all_pets = Pet.query.all()
    return render_template("index.html", pets = all_pets)

@app.route('/add', methods = ['GET', 'POST'])
def show_add_pet_form():
    """Pet add form; handle adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name = name,
                      species = species,
                      photo_url = photo_url,
                      age = age,
                      notes = notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name}")
        return redirect("/add")

    else:
        return render_template("add.html", form = form)
        # why does it not work if the html is named add_pet.html?


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_edit_pet_form(pet_id):
    """Show pet edit form and handle edit."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Pet {pet_id} updated!")
        return redirect(f"/{pet_id}")

    else:
        return render_template("/edit.html", form = form, pet = pet)
