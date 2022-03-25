import sentry_sdk

from flask import Flask, request, redirect
from flask_swagger_ui import get_swaggerui_blueprint

from converter.config_handler import config_handler
from converter.utils import get_settings, get_logging
import converter.api as awesomeapi

settings = get_settings()

if settings['env'].lower() == 'prod':
    sentry_sdk.init(settings['dns_sentry'])

app = Flask(__name__)

# swagger specific
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Converter"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/')
def root():
    return redirect('/swagger')


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return 'app running', 200


@app.route('/converter', methods=['POST'])
def converter():
    if len(request.data) == 0:
        return 'Body is required', 400
    data = request.get_json()

    if 'price' not in data:
        get_logging().warning('Field price is required on body')
        return 'Field price is required on body', 400

    if not type(data['price']) == float and not type(data['price']) == int:
        get_logging().warning('Field price is invalid - field: "{}"'.format(data['price']))
        return 'Field price is invalid', 400

    if data['price'] <= 0:
        get_logging().warning('Field price is negative or zero - field: "{}"'.format(data['price']))
        return 'Field price is invalid', 400

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
