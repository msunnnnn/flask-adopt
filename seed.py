from models import Pet, db
from app import app

db.drop_all()
db.create_all()


# add pet
floki = Pet(name = "Floki", species = "Doberman", photo_url = 'https://cdn.shopify.com/s/files/1/2456/1591/files/ashthegermanshepherd_large.JPG?v=1588952527', age = "baby", available = False)

biscuit = Pet(name = "Biscuit", species = "Cute", age = "young", available = False)

ruby = Pet(name = "Ruby", species= "dog", age = "senior", available = True)

db.session.add(floki)
db.session.add(biscuit)
db.session.add(ruby)
db.session.commit()