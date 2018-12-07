from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models.user import *

class Register(FlaskForm):
	username = StringField('Username', validators = [DataRequ ired(), Length(min = 2, max = 20)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirm_password = PasswordField('Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('sign up')
	def validate_username(self, username):
		user = user.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError('username taken already')

	def validate_email(self, Email):
		user = user.query.filter_by(email = email.data).first()
		if user:
			raise ValidationError('email taken already')


	#login formself
class LoginForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


	#business form
class BusinessForm(FlaskForm):
   name = StringField('Business name', validators = [DataRequired()])
   owner = StringField('Owners name', validators = [DataRequired()])
   location = StringField('Location', validators = [DataRequired()])
   date = StringField('date registered', validators = [DataRequired()])	


