from flask import render_template
from . import main


@main.route('/')
def chat():
    return render_template('chat.html')

