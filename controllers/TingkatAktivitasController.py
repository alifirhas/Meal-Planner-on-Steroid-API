from flask import jsonify
from flask_restful import Resource
from models.TingkatAktivitas import TingkatAktivitas, GenderEnum

class TingkatAktivitasController(Resource):
    def get(self):
        try:
            aktivitas = TingkatAktivitas.query.all()
            
            print(aktivitas)
            
            result = {
                "message": "Selamat datang di tingkat aktivitas get",
                "aktivitas": aktivitas
            }
            
            return jsonify(result)
        
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
