from flask import jsonify
from flask_restful import Resource
from models.User import User

class TestController(Resource):
    def get(self):
        try:
            users = User.query.all()
            result = {
                "message": "Selamat datang di test GET",
                "users": users
            }
            
            return jsonify(result)
        
        except Exception as e:
            print(e)
            return jsonify({"message": "Ada masalah"})

    def post(self):
        result = {"message": "Selamat datang di test POST"}

        return jsonify(result)

    def put(self):
        result = {"message": "Selamat datang di test PUT"}

        return jsonify(result)

    def delete(self):
        result = {"message": "Selamat datang di test DELETE"}

        return jsonify(result)
