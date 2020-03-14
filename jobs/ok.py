import click
from flask.cli import with_appcontext
import sys

@click.command('ok_run', help="ok run.")
@with_appcontext
def ok_run():
    print("ok")
    sys.exit(0)

if __name__ == '__main__':
    ok_run()
