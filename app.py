from flask import Flask, request
from flasgger import Swagger

from converter.config_handler import config_handler
import converter.api as awesomeapi

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    """Endpoint to healthcheck
    ---
    responses:
      200:
        description: app running
    """
    return 'app running', 200


@app.route('/converter', methods=['POST'])
def converter():
    """Endpoint to converter from REAL to USD, EUR and INR.
    ---
    parameters:
      - name: body
        in: body
        type: object
        properties:
          price:
            type: number
    responses:
      200:
        description: send result from converter
    """
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
