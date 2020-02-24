from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import videogame, member, rental
from flask_login import current_user

class RegistrationForm(FlaskForm):
    FirstName = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=1, max=30)
        ]
    )
    LastName = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=1, max=30)
        ]
    )
    HouseNameNo = StringField('House Name/NO',
        validators = [
            DataRequired(),
            Length(min=1, max=20)
        ]
    )
    Street = StringField('Street',
        validators = [
            DataRequired(),
            Length(min=1, max=20)
        ]
    )
    City = StringField('City',
        validators = [
            DataRequired(),
            Length(min=1, max=20)
        ]
    )
    County = StringField('County',
        validators = [
            DataRequired(),
            Length(min=1, max=20)
        ]
    )
    Postcode = StringField('Postcode',
        validators = [
            DataRequired(),
            Length(min=6, max=10)
        ]
    )
    EmailAddress = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    Password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('Password')
        ]
    )
    submit = SubmitField('Register')

    def validate_email(self, email):
        member = member.query.filter_by(email=EmailAddress.data).first()

        if member:
            raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
    EmailAddress = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    Password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

