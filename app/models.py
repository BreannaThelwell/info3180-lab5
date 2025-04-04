# Add any model classes for Flask-SQLAlchemy here

from app import db
import datetime

#'Movies' Table
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True) #primary key
    title = db.Column(db.String(100), nullable=False) #movie title (max 100 chars)
    description = db.Column(db.Text, nullable=False) #movie description
    poster = db.Column(db.String(255), nullable=False) #filename of poster
    created_at = db.Column(db.DateTime, default=datetime.datetime.now) #timestamp of creation 

    def __repr__(self):
        return f"<Movie {self.title}>"