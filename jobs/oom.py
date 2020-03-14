import click
from flask.cli import with_appcontext
from io import BytesIO

filename = './imgs/image.png'

@click.command('oom_run', help="oom run.")
@click.option('--count', type=click.INT, default=10)
@with_appcontext
def oom_run(count):
    imgs = []
    results = []
    for i in range(0, int(count)):
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

    print(results)

