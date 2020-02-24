from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import videogame, member, rental
from flask_login import login_user, current_user, logout_user, login_required
from application.forms import RegistrationForm, LoginForm

@app.route('/')
@app.route('/home')
def home():
    videogamedata = videogame.query.all()
    return render_template('home.html', title='Home', games=videogamedata)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
        if current_user.is_authenticated:
                return redirect(url_for('home'))
        form = RegistrationForm()
        if form.validate_on_submit():
                hash_pw = bcrypt.generate_password_hash(form.Password.data)
                addmember = member(
                        FirstName=form.FirstName.data,
                        LastName=form.LastName.data,
                        HouseNameNo=form.HouseNameNo.data,
                        Street=form.Street.data,
                        City=form.City.data,
                        County=form.County.data,
                        Postcode=form.Postcode.data,
                        EmailAddress=form.EmailAddress.data,
                        Password=hash_pw
                        )
                db.session.add(addmember)
                db.session.commit()

                return redirect(url_for('home'))
        return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        loginmember=member.query.filter_by(EmailAddress=form.EmailAddress.data).first()
        if loginmember and bcrypt.check_password_hash(loginmember.Password, form.Password.data):
            login_user(loginmember, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)
