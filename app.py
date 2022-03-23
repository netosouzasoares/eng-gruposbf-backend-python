from flask import Flask

app = Flask(__name__)


@app.route('/')
def healthcheck():
    return 'App running', 200
