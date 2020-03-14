from flask import Flask
from jobs import job
from apis import api

app = Flask(__name__)

api.init_app(app)

app.cli.add_command(job)
