#import flask package. Flask makes app objects.
from flask import Flask, render_template

# Creating the flask web server, makes the application
app = Flask(__name__)

# routes determine the location
@app.route("/")

# Define simple function
def home():
    return render_template('home.html')

#this will creat second page
@app.route("/about")
def preds():
    return render_template('about.html')
