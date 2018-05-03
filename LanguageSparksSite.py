from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)

bootstrap = Bootstrap (app)
moment = Moment (app)

@app.route('/')
def index ():
    return render_template ('index.html')

@app.route ('/services')
def services ():
    return render_template ('services.html')

@app.route ('/about')
def about ():
    return render_template ('about.html')

@app.route ('/links')
def links ():
    return render_template ('links.html')

@app.route ('/contact')
def contact ():
    return render_template ('contact.html')

@app.route('/user/<name>')
def user (name):
    return render_template ('user.html', name=name)

@app.errorhandler (404)
def page_not_found (e):
    return render_template ('404.html'), 404

@app.errorhandler (500)
def internal_server_error (e):
    return render_template ('500.html'), 500
