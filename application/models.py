from application import db, login_manager
from flask_login import UserMixin
from datetime import date, timedelta


class videogame(db.Model):
    VideoGameID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False, unique=True)
    Genre = db.Column(db.String(500), nullable=False, unique=True)
    Players = db.Column(db.String(100), nullable=False, unique=True)
    Rating = db.Column(db.String(100), nullable=False, unique=True)
    Platform = db.Column(db.String(100), nullable=False, unique=True)
    Rental = db.relationship('rental', backref='videogametorental', lazy=True)

    def __repr__(self):
         return ''.join([
             'Video Game ID: ', self.VideoGameID, '\r\n',
             'Description: ', self.Title, '\r\n', self.Genre, '\r\n', self.Players,'\r\n', self.Rating, '\r\n', self.Platform, '\r\n',
    ])

@login_manager.user_loader
def load_user(MemberID):
    return Member.query.get(int(MemberID))

class member(db.Model, UserMixin):
    MemberID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(30), nullable=False)
    LastName = db.Column(db.String(30), nullable=False)
    HouseNameNo = db.Column(db.String(30), nullable=False)
    Street = db.Column(db.String(30), nullable=False)
    City = db.Column(db.String(30), nullable=False)
    County = db.Column(db.String(30), nullable=True)
    Postcode = db.Column(db.String(30), nullable=False)
    EmailAddress = db.Column(db.String(150), nullable=False, unique=True)
    Password = db.Column(db.String(500), nullable=False)
    Rental = db.relationship('rental', backref='membertorental', lazy=True)

def __repr__(self):
   return ''.join([
            'Member ID: ', str(self.MemberID), '\r\n',
            'Name: ', self.FirstName, ' ', self.LastName, '\r\n',
            'Address: ', self.HouseNameNo, '\r\n', self.Street, '\r\n', self.City,
            '\r\n', self.County, '\r\n', self.Postcode, '\r\n',
            'Email: ', self.EmailAddress, '\r\n',
        ])

class rental(db.Model):
    RentalID = db.Column(db.Integer, primary_key=True)
    MemberID = db.Column(db.Integer, db.ForeignKey('member.MemberID'), primary_key=True, nullable=False)
    VideoGameID = db.Column(db.Integer, db.ForeignKey('videogame.VideoGameID'), primary_key=True, nullable=False)
    DateFrom = db.Column(db.DateTime, nullable=False, default=date.today)
    DateTo = db.Column(db.DateTime, nullable=False, default=date.today()+timedelta(days=5))

    def __repr__(self):
         return ''.join([
             'Rental ID: ', self.RentalID, '\r\n',
             'Member ID: ', self.MemberID, '\r\n',
             'Video Game ID: ', self.VideoGameID, '\r\n',
             'Date: ', self.DateFrom, '\r\n', self.DateTo
    ])
