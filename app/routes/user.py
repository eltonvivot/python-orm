from flask import Blueprint, request, jsonify
from ..models.user import User
from..utils.json import pretty_json

user_bp = Blueprint('user', '__name__', url_prefix='/users')

# GET all and POST
@user_bp.route('', methods=['POST', 'GET']) 
def handle_users():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = User(**data)
            new_user.save()
            return {"message": f"user has been created successfully.", "result": json.loads(new_user.to_json())}
        else:
            return {"error": "The request payload is not in JSON format"} 

    elif request.method == 'GET':
        results = User.objects()
        return {"count": len(results), "results": pretty_json(results)}

# Manage specific 
@user_bp.route('/<user_name>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(user_name):
    user = User.objects(name=user_name).first()
    if not user:
        return jsonify({'error': 'data not found'})

    if request.method == 'GET':
        return pretty_json(user)

    elif request.method == 'PUT':
        data = request.get_json()
        from_json(data, created=True)
        user.save()
        return {"message": f"user {user.name} successfully updated"}

    elif request.method == 'DELETE':
        user.delete()
        return {"message": f"User {user.name} successfully deleted."}