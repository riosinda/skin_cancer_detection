# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SkinData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    anatom_site = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    ethnic_group = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(10), nullable=True)  # BCC or SCC result
