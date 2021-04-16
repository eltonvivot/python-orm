from flask import Blueprint, request, jsonify
from ..utils.json import pretty_json
import sys
# ---- import models Class as resource_type endpoint ----
# from ..models.host_type import HostType as host_types
from ..models.host import Host as hosts
# from ..models.image import Image as images
# from ..models.member import Member as members
# from ..models.project import Project as projects
# from ..models.reservation import Reservation as reservations
# from ..models.ssh_key import SSHKey as ssh_keys
from ..models.user import User as users

resource_bp = Blueprint('resource', '__name__', url_prefix='/resources/<resource_type>')

# GET all and POST
@resource_bp.route('', methods=['POST', 'GET']) 
def handle_resources(resource_type):
    obj_type = getattr(sys.modules[__name__], resource_type)
    if request.method == 'POST': return handle_post(obj_type)
    elif request.method == 'GET': return handle_get_all(obj_type)

# Manage specific
@resource_bp.route('/<resource_name>', methods=['GET', 'PUT', 'DELETE'])
def handle_resource(resource_type, resource_name):
    obj_type = getattr(sys.modules[__name__], resource_type)
    resource = obj_type.objects(name=resource_name).first()
    if not resource: return jsonify({'error': 'data not found'})
    if request.method == 'GET': return handle_get(resource)
    elif request.method == 'PUT': return handle_put(resource)
    elif request.method == 'DELETE': return handle_delete(resource)

def handle_get_all(obj_type):
    results = obj_type.objects()
    return {"count": len(results), "results": pretty_json(results)}

def handle_get(resource):
    return {"result": pretty_json(resource)}

def handle_post(obj_type):
    if not request.is_json: return {"error": "The request payload is not in JSON format"}
    new_resource = obj_type(**request.get_json())
    new_resource.save()
    return {"message": f"resource has been created successfully.", "result": pretty_json(new_resource)}

def handle_put(resource):
    from_json(request.get_json(), created=True)
    resource.save()
    return {"message": f"resource successfully updated", "result": pretty_json(resource)}

def handle_delete(resource):
    resource.delete()
    return {"message": f"Resource successfully deleted.", "result": "OK."}