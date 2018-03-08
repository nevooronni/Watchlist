from flask import Flask
from .config import DevConfig
from flask_sqlalchemy import flask_sqlalchemy

bootstrap = bootstrap
db = SQLAlchemy#create a db instance 

#initializing application
app = Flask(__name__,instance_relative_config = True)#instance allows us to connect to the instance file

#setting up configuration 
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views