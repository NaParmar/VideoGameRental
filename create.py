from application import db
from application.models import videogame, member, rental

db.drop_all()
db.create_all()

