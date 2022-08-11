from re import template
from flask import Blueprint, render_template

web = Blueprint("web", __name__, static_folder="../static", template_folder="../templates")

@web.route("/")
def dashboard():
    return render_template('index.html')
