from flask import Flask, render_template
from typing import Dict

app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    return 'Hello World!'


@app.route('/test')
def test() -> Dict:
    return {'one': 1, 'two': 2}


@app.route('/entry')
def entry_page() -> str:
    return render_template('entry.html')


if __name__ == '__main__':
    app.run()
