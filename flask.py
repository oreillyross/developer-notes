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
