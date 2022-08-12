from . import db
from datetime import datetime
from dataclasses import dataclass
import enum

class GenderEnum(enum.Enum):    
    p = 0
    l = 1
    
@dataclass
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
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.String(100), nullable=True, default="/static/public/avatars/user-def.jpg")
    berat_badan = db.Column(db.Float(precision=3, decimal_return_scale=2), nullable=True)
    tinggi_badan = db.Column(db.Float(precision=3, decimal_return_scale=2), nullable=True)
    usia = db.Column(db.Float(precision=3, decimal_return_scale=2), nullable=True)
    gender = db.Column(db.Enum(GenderEnum), default=GenderEnum.l)
    imt = db.Column(db.Float(precision=3, decimal_return_scale=2), nullable=True)
    keseluruhan_energi = db.Column(db.Float(precision=6, decimal_return_scale=2), nullable=True)
    butuh_protein = db.Column(db.Float(precision=4, decimal_return_scale=2), nullable=True)
    butuh_karbo = db.Column(db.Float(precision=4, decimal_return_scale=2), nullable=True)
    butuh_lemak = db.Column(db.Float(precision=4, decimal_return_scale=2), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    tingkat_aktivitas_id = db.Column(db.Integer, db.ForeignKey("tingkat_aktivitas.id", ondelete='SET NULL'), nullable=True)
    
    tingkat_aktivitas =  db.relationship('TingkatAktivitas', backref='user', lazy=True, uselist=False)
    
