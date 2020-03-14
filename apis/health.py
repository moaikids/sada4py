from flask_restplus import Resource
from flask import request

class Health(Resource):
    def get(self):
        return {
            "status": "ok"
        }, 200
