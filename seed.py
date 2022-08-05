from models import Pet, db
from app import app

db.drop_all()
db.create_all()


# add pet
Floki = Pet(name = "Floki", species = "Doberman", age = "baby", available = False)

Biscuit = Pet(name = "Biscuit", species = "Cute", age = "young", available = False)


db.session.add(Floki)
db.session.add(Biscuit)
db.session.commit()