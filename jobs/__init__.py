from flask.cli import AppGroup
from .ok import ok_run
from .oom import oom_run

job = AppGroup('job')
job.add_command(ok_run)
job.add_command(oom_run)
