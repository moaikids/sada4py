from flask_restplus import Resource
from flask import request

class Sada(Resource):
    def get(self):
        return {
            "sada": "masashi"
        }, 200
