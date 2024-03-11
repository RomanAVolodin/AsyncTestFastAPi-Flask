import asyncio
from datetime import datetime
from time import sleep

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'Hello World! {datetime.now()}'


@app.route('/long')
def hello_world_long():
    sleep(10)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(threaded=False)

#  poetry run gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:5005 patched:app
