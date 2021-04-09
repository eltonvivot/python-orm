from flask import Flask, Blueprint, request
from ..models.user import User, db

user_bp = Blueprint('user', '__name__', url_prefix='/users')

# GET all and POST
@user_bp.route('', methods=['POST', 'GET'])
def handle_users():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = User(name=data['name'], login=data['login'], password=data['password'])
            new_user.save()
            return {"message": f"user {new_user.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        results = [user.to_json() for user in User.objects]
        return {"count": len(results), "users": results}

# Manage specific 
@user_bp.route('/<user_name>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(user_name):
    user = User.objects(name=user_name).first()
    if not user:
        return jsonify({'error': 'data not found'})

    if request.method == 'GET':
        return jsonify(user.to_json())

    elif request.method == 'PUT':
        data = request.get_json()
        user.login = data['login']
        user.password = data['password']
        user.save()
        return {"message": f"user {user.name} successfully updated"}

    elif request.method == 'DELETE':
        user.delete()
        return {"message": f"User {user.name} successfully deleted."}