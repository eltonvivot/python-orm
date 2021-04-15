from flask import Blueprint, request 
from ..models.ssh_key import SSHKey, db

ssh_key_bp = Blueprint('ssh_key', '__name__', url_prefix='/ssh_keys')

# GET all and POST
@ssh_key_bp.route('', methods=['POST', 'GET'])
def handle_ssh_keys():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_ssh_key = SSHKey(private_key=data["private_key"], public_key=data["public_key"])
            db.session.add(new_ssh_key)
            db.session.commit()
            return {"message": f"ssh_key has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        ssh_keys = SSHKey.query.all()
        results = [ ssh_key.to_json() for ssh_key in ssh_keys]

        return {"count": len(results), "ssh_keys": results}

# Manage specific 
@ssh_key_bp.route('/<ssh_key_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_ssh_key(ssh_key_id):
    ssh_key = SSHKey.query.get_or_404(ssh_key_id)
    # ssh_key = SSHKey.query.filter_by(name=ssh_key_id).first_or_404()

    if request.method == 'GET':
        response = ssh_key.to_json()
        return {"message": "success", "ssh_key": response}

    elif request.method == 'PUT':
        data = request.get_json()
        ssh_key.public_key = data['public_key']
        ssh_key.private_key = data['private_key']
        db.session.add(ssh_key)
        db.session.commit()
        return {"message": f"ssh_key {ssh_key} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(ssh_key)
        db.session.commit()
        return {"message": f"SSHKey {ssh_key} successfully deleted."}