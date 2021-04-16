import json
import datetime

def obj_to_json(obj):
    return json.dumps(serializable_to_json(obj))

def serializable_to_json(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()

    return obj.__dict__