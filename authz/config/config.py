from os import environ

class Config:
	
	##################### Application Configs #########################
	
	ENV = environ.get("TECHLAND_AUTHZ_ENV", "production")
	
	DEBUG = bool(int(environ.get("TECHLAND_AUTHZ_DEBUG", "0")))
	
	TESTING = bool(int(environ.get("TECHLAND_AUTHZ_TESTING", "0")))
	
	SECRET_KEY = environ.get("TECHLAND_AUTHZ_SECRET_KEY", "HARD-HARD-HARD-HARD-SECRET-KEY")

	##################### Database Configs ###########################
	
	SQLALCHEMY_DATABASE_URI = environ.get("TECHLAND_AUTHZ_DATABASE_URI", None)
	
	SQLALCHEMY_ECHO = DEBUG
	
	SQLALCHEMY_RECORD_QUERIES = DEBUG
	
	SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
