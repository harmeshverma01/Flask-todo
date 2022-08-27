from flask import Blueprint, jsonify, abort
from flask import request

todo_bp = Blueprint('todo', __name__, url_prefix='/todo')

@todo_bp.route('/add', methods={"GET","POST"})
def add_todo():
    if not request.json:
        abort(500)
        
    sno = request.json.get("sno", None)
    title = request.json.get("title", None)
    descriptions = request.json.get("descriptions", None)
    
    if sno is None or title is None or descriptions is None:
        return jsonify(message="Invalid Request"),500
    
    return ""
