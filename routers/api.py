from flask import Blueprint
from flask_restful import Api
from controllers.TestController import TestController

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

api.add_resource(TestController, "/test")
