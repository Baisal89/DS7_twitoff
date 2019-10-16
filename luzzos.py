#import flask package, flask makes app objects
from flask import Flask, render_template

#creating flask web server,  makes the application
app = Flask(__name__)

# routes determine the location
@app.route("/")

#Define simple function
def home():
    return render_template('home.html')

#this will creat second page
@app.route("/about")

def about():
    return render_template('about.html')

#this will creat third page
@app.route("/about/via")

def via():
    return render_template('via.html')
