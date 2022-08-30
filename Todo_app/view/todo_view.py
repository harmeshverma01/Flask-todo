from flask import Blueprint, jsonify, abort
from flask import request
from Todo_app.schema.todo import Todo

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
    
    return ({'message':'Created SuccessFully'})


@todo_bp.route('/todo-list', methods={"GET"})
def all_todo():
    if not request.json:
        abort(500)
    
    todos = Todo.query.all()
    result = []
    for todo in todos:
        todo_data = {}
        todo_data['sno']=todo.sno
        todo_data['title']=todo.title
        todo_data['descriptions']=todo.descriptions
        
        result.append(todo_data)
        return jsonify({'todos': result})
        