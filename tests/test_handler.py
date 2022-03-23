from converter import handler


def test_shoud_convert_from_real_to_usd():
    result = handler.usd(10, 4.86)
    assert result == '$2.06'


def test_shoud_convert_from_real_to_eur():
    result = handler.eur(10, 5.34)
    assert result == '1,87 €'


def test_shoud_convert_from_real_to_inr():
    result = handler.inr(10, 0.063)
    assert result == '₹158.73'
