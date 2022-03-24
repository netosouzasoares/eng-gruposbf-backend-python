import logging
from urllib.error import HTTPError
import requests
from dynaconf import settings
import logging

def get_coins_values():

    try:
        result = requests.get(settings['awesomea_api'])
        response = result.json()
        return {
            'USD': float(response['USDBRL']['bid']),
            'EUR': float(response['EURBRL']['bid']),
            'INR': float(response['INRBRL']['bid'])
        }
    except HTTPError:
        logging.error('get error from awesomeapi')
        return None