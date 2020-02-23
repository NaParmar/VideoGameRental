from application import db
from application.models import videogame

game1 = videogame(Title="SPIDER-MAN",
	Genre="Action-Adventure",
	Players="1 Player",
	Rating="16",
	Platform="PS4")

game2 = videogame(Title="SPIDER-MAN",
        Genre="Action-Adventure",
        Players="1 Player",
        Rating="16",
        Platform="XBOX")

game3 = videogame(Title="Overwatch",
        Genre="First Person Shooter",
        Players="Multiplayer",
        Rating="12+",
        Platform="PS4")

game4 = videogame(Title="Overwatch",
        Genre="First Person Shooter",
        Players="Multiplayer",
        Rating="12+",
        Platform="XBOX")

db.session.add(game1)
db.session.add(game2)
db.session.add(game3)
db.session.add(game4)
db.session.commit()
