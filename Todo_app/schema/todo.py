import app
from app.db import create_db
from app import db

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    descriptions = db.Column(db.Strings(500), unique=True, nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.sno} {self.title}"
    