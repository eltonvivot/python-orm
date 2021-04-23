from flask import Blueprint, request, jsonify
from ..utils.json import pretty_json
import sys
# ---- import models Class as data_type endpoint ----
from ..models.host_type import HostType as host_types
from ..models.host import Host as hosts
from ..models.image import Image as images
from ..models.member import Member as members
from ..models.project import Project as projects
from ..models.reservation import Reservation as reservations

data_bp = Blueprint('data', '__name__', url_prefix='/data/<data_type>')

# GET all and POST
@data_bp.route('', methods=['POST', 'GET']) 
def handle_all_data(data_type):
    obj_type = getattr(sys.modules[__name__], data_type)
    if request.method == 'POST': return handle_post(obj_type)
    elif request.method == 'GET': return handle_get_all(obj_type)

# Manage specific
@data_bp.route('/<data_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_specific_data(data_type, data_id):
    obj_type = getattr(sys.modules[__name__], data_type)
    data = obj_type.objects(id=data_id).first()
    if not data: return jsonify({'error': 'data not found'})
    if request.method == 'GET': return handle_get(data)
    elif request.method == 'PUT': return handle_put(data)
    elif request.method == 'DELETE': return handle_delete(data)

def handle_get_all(obj_type):
    results = obj_type.objects()
    return {"count": len(results), "results": pretty_json(results)}

def handle_get(data):
    return {"result": pretty_json(data)}

def handle_post(obj_type):
    if not request.is_json: return {"error": "The request payload is not in JSON format"}
    new_data = obj_type(**request.get_json())
    new_data.save()
    return {"message": f"data has been created successfully.", "result": pretty_json(new_data)}

def handle_put(data):
    from_json(request.get_json(), created=True)
    data.save()
    return {"message": f"data successfully updated", "result": pretty_json(data)}

def handle_delete(data):
    data.delete()
    return {"message": f"Resource successfully deleted.", "result": "OK."}