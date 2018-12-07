from app import app, db, bcrypt
from flask import render_template, url_for, redirect
from flask_login import login_user, logout_user, current_user, login_required
from app.forms.register import Register  

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/register', methods = ['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home')) 
	form = Register()
	if form.validate_on_submit():
		user = User(username = form.username.data, email = form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Account for has been created', 'success')
		return redirect(url_for('login'))
	return render_template('signup.html', form =form)


@app.route('login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password):
			login_user(user, remember = form.remember.data)
			return redirect(url_for('home'))
		else:
			flash('login unsuccessful, check your credentials')
	return render_template('login.html', title= 'login', form = form)


@app.route('/logout')
def logout():
	logout_user()
return redirect(url_for('home'))

@app.route('/Business')
def new_business():
	return render_template('business_reg.html')