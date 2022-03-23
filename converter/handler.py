

def usd(price, value_usd):
    return format_value((float(price) / value_usd))


def eur(price, value_eur):
    return format_value((float(price) / value_eur))


def inr(price, value_inr):
    return format_value((float(price) / value_inr))


def format_value(value):
    return "{:,.2f}".format(value)
