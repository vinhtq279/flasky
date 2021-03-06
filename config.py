import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	MAIL_SERVER = os.environ.get('MAIL_SERVER', 'mail.vnpt-technology.vn')
	MAIL_PORT = int(os.environ.get('MAIL_PORT', '25'))
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['false', 'off', '0']
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'Flasky Admin <vinhtq@vnpt-technology.vn>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	@staticmethod
	def init_app(app):
		pass

class 
