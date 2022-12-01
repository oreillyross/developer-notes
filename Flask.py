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




