from flask import Blueprint
from flask_restful import Api
from controllers.UserController import UserController
from controllers.TingkatAktivitasController import TingkatAktivitasController

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(UserController, "/user")
api.add_resource(TingkatAktivitasController, "/tingkat-aktivitas")
