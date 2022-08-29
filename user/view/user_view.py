from flask import Blueprint, jsonify, abort, make_response
from werkzeug.security import check_password_hash
from flask import request
from user.schema.user import User
from app.db import db
import jwt


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/user', methods={"POST", "GET"})
def add_user():
    if not request.json:
        abort(500)
    
    form = [add_user]
    id = request.json.get("id", None),
    username = request.json.get("name", None),
    email = request.json.get("email", None),
    password = request.json.get("password", None)
 
    if id is None or username is None or email is None or password is None:
        return jsonify(message="Invalid Request"),500
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username, email, password)
            db.session.add(user)
            db.session.commit()
    return jsonify({'message': 'Created Successfully'})



@auth_bp.route('/login', methods={"POST"})
def login():
    auth = request.authorizations
    if not request.json:
        abort(500)
        
    if not auth or auth.email or auth.password:
        return make_response('could not verify', 401, {'Authentication' : '"login Required"'})
        
    user = User.query.filter_by(email=auth.email).first()
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({"email": "email", "password":"password"})
        return jsonify({'token':token})
    return make_response('could not verify', 401, {'Authentication': 'login Required'})



auth_bp.route('/users', methods={"GET"})
def user_list():
    if not request.json:
        abort(500)
        
    users = User.query.all()
    result = []
    for user in users:
        user_data = {}
        user_data['id']=user.id
        user_data['name']=user.name
        user_data['email']=user.email
        user_data['password']=user.password
        
        result.append(user_data)
    return jsonify({'users':result})    
    