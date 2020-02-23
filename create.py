from application import db
from application.models import videogame, member, videogame

db.drop_all()
db.create_all()

