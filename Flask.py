# Web requests
# client (browser) -> type in url -> server locates webpage -> page is returned
# Happens over http protocol

# Dynamic websites
# File on the server is customised and generated on the fly 
# Web application server is needed

# Web frameworks

# Generate HTML based on specific request and other factors
# re-use html elements across multiple pages on a site
# maintain sessions
# query database

# Parts of a web application
# 1. input forms
# 2. URL routing -> map URL to a function
#       Key value pairs, route url (qnwel.com/about) is the key, value is the function about()

@app.route("/")
def home():
    return "Hello World!"
    # OR return html
    """
    <html>
       ....
    </html>
    """
# or post request
@app.route("/review", methods =["GET", "POST"])
def review():
    # logic here to process request
    return """<html>..."""
    # alternatively use the function to return a separate page, business logic and view logic separation
    render_template("review.html")
# 3. HTML templates - Flask uses Jinja
#   define a base template with all required components
#   put in placeholders for the sections to be overridden, to be customized
# 4. Sessions
# 5. DB connections 
#  Flask extensions extend the micro web framework flask
# HTML Forms - WTForms (flask-wtf) 
# define python objects -> html generated automatically
# DB Connections - SQLAlchemy
# BCrypt and Login packages for session management

# WSGI spec
# This is useful to be able to host on many different servers


#! sudo easy_install pip

#! sudo pip install --upgrade pip

#! pip install virtualenv

#! virtualenv flaskenv -p python3

#! cd flaskenv # bin include bin, inside bin is activate

#! . flaskenv/bin/activate

#! pip install Flask

#! python # Python 3.7.4

>>> import flask
>>> exit()

# should work without error

## Basic flask app

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return """
  <!doctype html>
     <head>
        <title>Welcome</title>
     </head>
     <body>
         ...
     </body>
  </html>
"""


if __name__ == '__main__':
  app.run(debug=True)


### Using templates

from flask impoert Flask, render_template

#! create a folder called templates

@app.route('/')
def home():
  return render_template('home.html)

#### Boilerplate html
                         
# https://www.initializer.com
                         
# click on responsive, mobile first, include 404 page, download it
                         
# unzip file and copy all files into the static folder

#### navigating pages programatically
# in a html file, you also need to make sure the @app.route('/add') is defined in main page
{{url_for('add')}} # url_for will look for add function route
 
# Using Jinja templates
                         
#! create a base.html fil in templates directory
# make use of Jinja template definition language

<html>
    <title> {% block title %} {% endblock %} </title>
    <body>
       {% block content %}
       {%  endblock %}
    </body>
</html>

### inheriting the base Jinja template, create a new file project.html

{% extends "base.html" %}

{%block title %} Project - welcome {% endblock%}
                         
{%block content %} Your own content {% endblock%}


