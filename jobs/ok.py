import click
from flask.cli import with_appcontext

@click.command('ok_run', help="ok run.")
@with_appcontext
def ok_run():
    print("ok")

if __name__ == '__main__':
    ok_run()
