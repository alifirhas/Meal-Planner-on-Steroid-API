import string
from . import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class User(db.Model):
    id: int
    name: str
    email: str
    username: str
    password: str
    avatar: str
    date_created: str
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.String(100), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    