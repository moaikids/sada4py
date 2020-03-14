from flask_restplus import Api
from .health import Health
from .oom import OOM
from .shutdown import ShutDown

api = Api()

api.add_resource(Health, '/health')
api.add_resource(OOM, '/oom')
api.add_resource(ShutDown, '/shutdown')
