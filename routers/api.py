from email import message
from re import template
from flask import Blueprint, render_template

api = Blueprint("api", __name__, static_folder="../static", template_folder="../templates")

@api.route("/")
def dashboard():
    return "Selamat datang di MPS RESTful-API"
