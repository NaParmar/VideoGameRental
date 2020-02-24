from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import videogame, member, rental
from flask_login import login_user, current_user, logout_user, login_required
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm

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

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
        form = UpdateAccountForm()
        if form.validate_on_submit():
                current_user.FirstName = form.FirstName.data
                current_user.LastName = form.LastName.data
                current_user.HouseNameNo = form.HouseNameNo.data
                current_user.Street = form.Street.data
                current_user.City = form.City.data
                current_user.County = form.County.data
                current_user.Postcode = form.Postcode.data
                current_user.EmailAddress = form.EmailAddress.data
                db.session.commit()
                return redirect(url_for('account'))
        elif request.method == 'GET':
                form.FirstName.data = current_user.FirstName
                form.LastName.data = current_user.LastName
                form.HouseNameNo.data = current_user.HouseNameNo
                form.Street.data = current_user.Street
                form.City.data = current_user.City
                form.County.data = current_user.County
                form.Postcode.data = current_user.Postcode
                form.EmailAddress.data = current_user.EmailAddress
        return render_template('account.html', title='Account', form=form)

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    currentmember = current_user.MemberID
    rentals = rental.query.filter_by(MemberID=currentmember).all()
    for rentalorder in rentals:
        db.session.delete(rentalorder)
    account = member.query.filter_by(MemberID=currentmember).first()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))
