# Add any form classes for Flask-WTF here 

#necessary imports
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileRequired 

#MovieForm class
class MovieForm (FlaskForm):
    title = StringField( #string title field required and limited to 100 characters
        'Title',
        validators =[
            DataRequired(message="Title is required."),
            Length(max=100, message="Title cannot exceed 100 characters.")
        ]
    )
    description = TextAreaField( #text field for description, required
        'Description',
        validators=[
            DataRequired(message="Please provide a description of the movie.")
        ]
    )
    poster = FileField( #field for movie poster image. accepts only image files
        'Poster',
        validators=[
            FileRequired(message="Movie Poster image is required."),
            FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
        ]
    )