from flask import render_template
from . import main

@main.route('/news')
def news():
    return None
