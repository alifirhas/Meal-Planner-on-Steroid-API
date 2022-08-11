from flask import jsonify
from flask_restful import Resource


class TestController(Resource):
    def get(self):
        result = {"message": "Selamat datang di test GET"}

        return jsonify(result)

    def post(self):
        result = {"message": "Selamat datang di test POST"}

        return jsonify(result)

    def put(self):
        result = {"message": "Selamat datang di test PUT"}

        return jsonify(result)

    def delete(self):
        result = {"message": "Selamat datang di test DELETE"}

        return jsonify(result)
