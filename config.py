import os

basedir = os.path.abspath(os.path.dirname(__file__))
class config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'gerarihia'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
				'sqlite:///' + os.path.join(basedir, 'kasa.db')
	DEBUG = False