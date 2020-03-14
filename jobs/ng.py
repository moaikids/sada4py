import click
from flask.cli import with_appcontext
import sys

@click.command('ng_run', help="ng run.")
@with_appcontext
def ng_run():
    print("ng")
    sys.exit(1)

if __name__ == '__main__':
    ng_run()
