from flask import Flask, request

from converter.config_handler import config_handler
import converter.api as awesomeapi

app = Flask(__name__)


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return 'app running', 200


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

    bid_values = awesomeapi.get_coins_values()

    if not bid_values:
       return 'Internal Error', 500

    return {
        'USD': config_handler['USD'](price, bid_values['USD']),
        'EUR': config_handler['EUR'](price, bid_values['EUR']),
        'INR': config_handler['INR'](price, bid_values['INR'])
    }, 200
