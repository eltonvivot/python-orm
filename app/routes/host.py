from flask import Blueprint, request, jsonify
from ..models.host import Host

host_bp = Blueprint('host', '__name__', url_prefix='/hosts')

# GET all and POST
@host_bp.route('', methods=['POST', 'GET']) 
def handle_hosts():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_host = Host()
            new_host.serialize(data) 
            new_host.save()
            return {"message": f"host {new_host.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"} 

    elif request.method == 'GET':
        results = [ host.to_json() for host in Host.objects]
        return {"count": len(results), "hosts": results}

# Manage specific 
@host_bp.route('/<host_name>', methods=['GET', 'PUT', 'DELETE'])
def handle_host(host_name):
    host = Host.objects(name=host_name).first()
    if not host:
        return jsonify({'error': 'data not found'})

    if request.method == 'GET':
        return jsonify({"result": host.to_json()})

    elif request.method == 'PUT':
        data = request.get_json()
        host.serialize(data)
        host.save()
        return {"message": f"host {host.name} successfully updated"}

    elif request.method == 'DELETE':
        host.delete()
        return {"message": f"Host {host.name} successfully deleted."}