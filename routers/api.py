from flask import Blueprint
from flask_restx import Api
from controllers.API.UserController import UserController
from controllers.API.TingkatAktivitasController import TingkatAktivitasController

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(UserController, "/user")
api.add_resource(TingkatAktivitasController, "/tingkat-aktivitas")
