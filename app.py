from flask import Flask, request

from converter.config_handler import config_handler

app = Flask(__name__)


@app.route('/', methods=['GET'])
def healthcheck():
    return 'App running', 200


@app.route('/converter', methods=['POST'])
def converter():
    if len(request.data) == 0:
        return 'Body is required', 400
    data = request.get_json()

    if 'price' not in data:
        return 'Field price is required on body', 400

    return orchestrator(data)


def orchestrator(data):
    price = data['price']

    return {
        'USD': config_handler['USD'](price),
        'EUR': config_handler['EUR'](price),
        'INR': config_handler['INR'](price)
    }, 200
