from flask import jsonify
from flask_restx import Resource, marshal_with
from models.TingkatAktivitas import TingkatAktivitas, aktivitas_fields
from models.Gender import Gender

class TingkatAktivitasController(Resource):
    @marshal_with(aktivitas_fields)
    def get(self):
        try:
            aktivitas = TingkatAktivitas.query.all()
            gender = Gender.query.all()
            
            return aktivitas
        
        except Exception as e:
            print(e)
            return jsonify({"message": "Ada masalah"})

    def post(self):
        result = {"message": "Selamat datang di tingkat aktivitas POST"}

        return jsonify(result)

    def put(self):
        result = {"message": "Selamat datang di tingkat aktivitas PUT"}

        return jsonify(result)

    def delete(self):
        result = {"message": "Selamat datang di tingkat aktivitas DELETE"}

        return jsonify(result)
