from . import db
from datetime import datetime
from flask_restx import fields
from .TingkatAktivitas import aktivitas_fields

user_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "password": fields.String,
    "avatar": fields.String,
    "berat_badan": fields.Float,
    "tinggi_badan": fields.Float,
    "usia": fields.Integer,
    "gender": fields.String,
    "imt": fields.Float,
    "keseluruhan_energi": fields.Float,
    "butuh_protein": fields.Float,
    "butuh_karbo": fields.Float,
    "butuh_lemak": fields.Float,
    "tingkat_aktivitas": fields.Nested(aktivitas_fields),
    "date_created": fields.DateTime,
}

class User(db.Model):
    __tablename__ = 'user'
    
    id: int
    name: str
    email: str
    username: str
    password: str
    avatar: str
    berat_badan: float
    tinggi_badan: float
    usia: int
    gender: str
    imt: float
    keseluruhan_energi: float
    butuh_protein: float
    butuh_karbo: float
    butuh_lemak: float
    date_created: str
    tingkat_aktivitas_id: int
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.String(100), nullable=True, default="/static/public/avatars/user-def.jpg")
    berat_badan = db.Column(db.Float(precision=3, decimal_return_scale=2), nullable=True)
    tinggi_badan = db.Column(db.Float(precision=3, decimal_return_scale=2), nullable=True)
    usia = db.Column(db.Float(precision=3, decimal_return_scale=2), nullable=True)
    gender = db.Column(db.String(2), db.ForeignKey("gender.name", ondelete='SET NULL'))
    imt = db.Column(db.Float(precision=3, decimal_return_scale=2), nullable=True)
    keseluruhan_energi = db.Column(db.Float(precision=6, decimal_return_scale=2), nullable=True)
    butuh_protein = db.Column(db.Float(precision=4, decimal_return_scale=2), nullable=True)
    butuh_karbo = db.Column(db.Float(precision=4, decimal_return_scale=2), nullable=True)
    butuh_lemak = db.Column(db.Float(precision=4, decimal_return_scale=2), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    tingkat_aktivitas_id = db.Column(db.Integer, db.ForeignKey("tingkat_aktivitas.id", ondelete='SET NULL'), nullable=True)
    
    def __repr__(self):
        return f"User(id={self.id}, \
            name={self.name}, \
            email={self.email}, \
            username={self.username}, \
            avatar={self.avatar}, \
            berat_badan={self.berat_badan}, \
            tinggi_badan={self.tinggi_badan}, \
            usia={self.usia}, \
            name={self.name}, \
            imt={self.gender} \
            keseluruhan_energi={self.keseluruhan_energi} \
            butuh_protein={self.butuh_protein} \
            butuh_karbo={self.butuh_karbo} \
            butuh_lemak={self.butuh_lemak} \
            tingkat_aktivitas={self.tingkat_aktivitas_id} \
            date_created={self.date_created})"
    
