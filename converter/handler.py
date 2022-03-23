
from babel.numbers import format_currency


def usd(price, value_usd):
    return format_currency((float(price) / value_usd), 'USD', locale='en_US')


def eur(price, value_eur):
    return format_currency((float(price) / value_eur), 'EUR', locale='fr_FR')


def inr(price, value_inr):
    return format_currency((float(price) / value_inr), 'INR', locale='en_IN')
