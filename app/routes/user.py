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
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"user {new_user.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        users = User.query.all()
        results = [ user.to_json() for user in users]

        return {"count": len(results), "users": results}

# Manage specific 
@user_bp.route('/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    user = User.query.get_or_404(user_id)
    # user = User.query.filter_by(name=user_id).first_or_404()

    if request.method == 'GET':
        response = user.to_json()
        return {"message": "success", "user": response}

    elif request.method == 'PUT':
        data = request.get_json()
        user.name = data['name']
        user.login = data['login']
        user.password = data['password']
        db.session.add(user)
        db.session.commit()
        return {"message": f"user {user.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user.name} successfully deleted."}