from urllib.error import HTTPError
import requests


def get_coins_values():

    try:
        # TODO: set url on config
        result = requests.get('https://economia.awesomeapi.com.br/last/USD,EUR,INR')
        response = result.json()
        return {
            'USD': float(response['USDBRL']['bid']),
            'EUR': float(response['EURBRL']['bid']),
            'INR': float(response['INRBRL']['bid'])
        }
    except HTTPError:
        # TODO: add logger here
        print('error to get values from awesomeapi')
        return None