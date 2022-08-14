from . import db
from flask_restx import fields

gender_field = {
    "name": fields.String,
}

class Gender(db.Model):
    __tablename__ = "gender"

    name: str
    
    name = db.Column(db.String(2), nullable=False, primary_key=True)
    
    user = db.relationship("User", backref="gender")
    tingkat_aktivitas = db.relationship("TingkatAktivitas", backref="gender")
