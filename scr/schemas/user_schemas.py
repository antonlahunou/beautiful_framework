GET_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "gender": {"type": "string", "enum": ["male", "female"]},
        "status": {"type": "string", "enum": ["active", "inactive"]}
    },
    "required": ["id", "name"],
    "additionalProperties": False
}

# {'id': 8435819, 'name': 'Gangesh Namboothiri', 'email': 'gangesh_namboothiri@keeling.example', 'gender': 'female', 'status': 'active'}