from flask_sqlalchemy import SQLAlchemy
from app.__init__ import create_app

def create_db():
    create_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    create_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(create_app)
    return db

