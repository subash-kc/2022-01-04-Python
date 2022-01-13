"""
Handle only one request one time
not good for developer

Flask is a small and lightweight Python web framework that provides useful tools and features that make creating web applications in Python easier.
It gives developers flexibility and is a more accessible framework for new developers since you can build a
web application quickly using only a single Python file

Flask is a web development framework created in Python language.
This Framework is based on the robust foundation of Jinja2 templates engine and Werkzeug comprehensive WSGI web application library.
"""

# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function


@app.route("/")
def hello_world():
   return "Hello World"

@app.route("/subash")
def hello_subash():
   return "Hello, Namaste,  Subash KC"

#not a good way to implement below code in flask
def hello_world1():
   return "hello world"
app.add_url_rule("/hello", "hello", hello_world1)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE