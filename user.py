from app import db, login_manager
from flask_login import UserMixin 

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	__tablenam__ = 'users'
	user_id = db.Column(db.Integer, primary_key = True, nullable = False)
	name = db.Column(db.String(), nullable = False)
	email = db.Column(db.String(), nullable = False)
	password = db.Column(db.String(), nullable = False)

	def __repr__(self):
		return f'User{self.name}'


class Business(db.Model):
	__tablenam__ = 'business'
	id = db.Column(db.Integer, primary_key = True, nullable = False)
	Business_name = db.Column(db.String(), nullable = False)
	Business_location = db.Column(db.String(), nullable = False)
	Business_owner = db.Column(db.String(), nullable = False)
	Business_desc = db.Column(db.String(), nullable = False)

	def __repr__(self):
		return f'User: {self.business_name}, {self.Business_location}, {self.Business_owner}, {self.Business_desc}'