from flask import Flask
from flask_cors import CORS #forntend requests
from flask_sqlalchemy import SQLAlchemy #import for db
from flask_migrate import Migrate #import for db
from flask_wtf.csrf import CSRFProtect #required import 
from .config import Config

app = Flask(__name__)
CORS(app)
csrf = CSRFProtect(app)
app.config.from_object(Config)

#initializa extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import Movie #ensure flask-migrate picks up model

from app import views