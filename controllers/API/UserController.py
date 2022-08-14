import marshal
from flask import jsonify
from flask_restx import Resource, marshal_with
from models.User import User, user_fields

class UserController(Resource):
    @marshal_with(user_fields, envelope='users')
    def get(self):
        try:      
            users = User().query.all()
                
            return users
        
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
