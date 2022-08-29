from flask import Blueprint, jsonify, abort
from flask import request

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/user', methods={"POST", "GET"})
def add_user():
    if not request.json:
        abort(500)
    
    name = request.json.get("name", None)
    email = request.json.get("email", None)
    role = request.json.get("role", None)
    
    if name is None or email is None:
        return jsonify(message="Invalid Request"),500
    
    
    return ""
