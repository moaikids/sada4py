from flask_restplus import Resource
from flask import request
from io import BytesIO

filename = './imgs/image.png'

class OOM(Resource):
    def get(self):
        count = int(request.args.get("count", "10"))
        imgs = []
        results = []
        for i in range(0, count):
            id = i % 10
            with open(filename.format(id), 'rb') as f:
                binary = f.read()
            img_size = len(binary)

            result = {
                "image_id": i,
                "image_size": img_size
            }
            imgs.append(binary)
            results.append(result)
        return results, 200

