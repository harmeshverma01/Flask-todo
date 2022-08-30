from flask import Flask
from user.view.user_view import auth_bp
from Todo_app.view.todo_view import todo_bp
from app.db import create_db


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    app.register_blueprint(todo_bp)
    return app
    
db = create_db()

if __name__ == '__main__':
    create_app()