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
def add_pet():
    """Pet add form; handle adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name = name, species = species,photo_url = photo_url,
                      age = age, notes = notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name}")
        return redirect("/add")

    else:
        return render_template("add.html", form = form)
        # why does it not work if the html is named add_pet.html?


@app.route("/<int:uid>", methods=["GET", "POST"])
def edit_user(uid):
    """Show pet edit form and handle edit."""

    user = Pet.query.get_or_404(uid)
    form = EditPetForm(obj=user)

    if form.validate_on_submit():
        user.photo_url = form.photo_url.data
        user.notes = form.notes.data
        user.available = form.available.data
        db.session.commit()
        flash(f"Pet {uid} updated!")
        return redirect(f"/{uid}")

    else:
        return render_template("/edit.html", form=form, pet = user)
