from urllib.error import HTTPError
from converter.utils import get_settings, get_logging

import requests


def get_coins_values():
    settings = get_settings()
    try:
        result = requests.get(settings['awesomea_api'])
        response = result.json()
        return {
            'USD': float(response['USDBRL']['bid']),
            'EUR': float(response['EURBRL']['bid']),
            'INR': float(response['INRBRL']['bid'])
        }
    except HTTPError:
        get_logging().error('error from awesomea api')
        return None
