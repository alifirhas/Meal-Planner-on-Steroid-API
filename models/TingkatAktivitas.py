from . import db
from datetime import datetime
from flask_restx import fields

aktivitas_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "nilai_aktivitas": fields.Float,
    "gender": fields.String,
    "date_created": fields.DateTime,
}

class TingkatAktivitas(db.Model):
    __tablename__ = "tingkat_aktivitas"

    id: int
    name: str
    gender: str
    nilai_aktivitas: float
    date_created: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(2), db.ForeignKey("gender.name", ondelete='SET NULL'))
    nilai_aktivitas = db.Column(
        db.Float(precision=3, decimal_return_scale=2), nullable=False
    )
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref="tingkat_aktivitas")

    def __repr__(self):
        return f"TingkatAktivitas(id={self.id}, name={self.name}, gender={self.gender} date_created={self.date_created})"
    
    def json(self):
        data = {"id": self.id, "name": self.name, "gender": self.gender, "date_crated": self.date_created}
        return data
