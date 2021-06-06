from flask import Flask
from typing import Dict

app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    return 'Hello World!'


@app.route('/test')
def test() -> Dict:
    return {'one': 1, 'two': 2}


if __name__ == '__main__':
    app.run()
