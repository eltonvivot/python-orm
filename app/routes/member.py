from flask import Blueprint, request, jsonify
from ..models.member import Member

member_bp = Blueprint('member', '__name__', url_prefix='/members')

# GET all and POST
@member_bp.route('', methods=['POST', 'GET']) 
def handle_members():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_member = Member()
            new_member.serialize(data) 
            new_member.save()
            return {"message": f"member {new_member.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"} 

    elif request.method == 'GET':
        results = [ member.to_json() for member in Member.objects]
        return {"count": len(results), "members": results}

# Manage specific 
@member_bp.route('/<member_name>', methods=['GET', 'PUT', 'DELETE'])
def handle_member(member_name):
    member = Member.objects(name=member_name).first()
    if not member:
        return jsonify({'error': 'data not found'})

    if request.method == 'GET':
        return jsonify({"result": member.to_json()})

    elif request.method == 'PUT':
        data = request.get_json()
        member.serialize(data)
        member.save()
        return {"message": f"member {member.name} successfully updated"}

    elif request.method == 'DELETE':
        member.delete()
        return {"message": f"Member {member.name} successfully deleted."}