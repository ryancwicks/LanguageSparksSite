from flask import render_template
from . import main

@main.route('/')
def index ():
    return render_template ('index.html')

@main.route ('/services')
def services ():
    return render_template ('services.html')

@main.route ('/about')
def about ():
    return render_template ('about.html')

@main.route ('/links')
def links ():
    return render_template ('links.html')

@main.route ('/contact')
def contact ():
    return render_template ('contact.html')
