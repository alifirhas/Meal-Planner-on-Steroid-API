from . import db
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum

class GenderEnum(int, Enum):
    
    p = 0
    l = 1
    
    # def __repr__(self):
    #     return f"{self.name}"


@dataclass
class TingkatAktivitas(db.Model):
    __tablename__ = "tingkat_aktivitas"

    id: int = field(init=False)
    name: str
    gender: GenderEnum
    nilai_aktivitas: float
    date_created: datetime

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Enum(GenderEnum), nullable=False)
    nilai_aktivitas = db.Column(
        db.Float(precision=3, decimal_return_scale=2), nullable=False
    )
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
