from converter import handler


def test_shoud_convert_from_real_to_usd():
    result = handler.usd(10, 4.86)
    assert result == '2.06'


def test_shoud_convert_from_real_to_eur():
    result = handler.eur(10, 5.34)
    assert result == '1.87'


def test_shoud_convert_from_real_to_inr():
    result = handler.inr(10, 0.063)
    assert result == '158.73'

def test_should_format_price():
    result = handler.format_value(10.12121212)
    assert result == '10.12'


def test_should_format_price_inr():
    result = handler.format_value(0.06326)
    assert result == '0.06'
