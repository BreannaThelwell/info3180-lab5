"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db #added db import
from app.forms import MovieForm #exercise 1 form
from app.models import Movie #exercise 2 db
from flask import request, jsonify, send_file, send_from_directory #render_template
from flask_wtf.csrf import generate_csrf #required import
from werkzeug.utils import secure_filename #for uploads folder
import os


#exercise 3 new route
@app.route('/api/v1/movies', methods=['POST'])
def movies():
    form = MovieForm() #instantiate form class
    if form.validate_on_submit(): #validate form upload on submit
        #get form data
        title = form.title.data
        description = form.description.data
        poster = form.poster.data

        #secure filename
        filename = secure_filename(poster.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #save file to uploads folder
        poster.save(filepath)

        #save movie to database
        movie = Movie(title=title, description=description, poster=filename)
        db.session.add(movie)
        db.session.commit()

        # Return success JSON
        return jsonify({
            "message": "Movie Successfully added",
            "title": title,
            "poster": filename,
            "description": description
        }), 201
    else:
        # Return form errors
        return jsonify({
            "errors": form_errors(form)
        }), 400

#exercise 5 
# GET all movies
@app.route('/api/v1/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    movies_list = [{
        'id': movie.id,
        'title': movie.title,
        'description': movie.description,
        'poster': f'/api/v1/posters/{movie.poster}'
    } for movie in movies]
    return jsonify({'movies': movies_list})

#for uploaded posters
@app.route('/api/v1/posters/<filename>')
def get_poster(filename):
    upload_folder = os.path.join(os.getcwd(), 'uploads') #path
    return send_from_directory(upload_folder, filename)


#securely send token
@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page not found"), 404 #removed template and used json instead