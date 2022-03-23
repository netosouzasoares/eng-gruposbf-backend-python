from app import orchestrator
import mock


def test_should_return_values():
    mock_api_result = {'USD': 4.8403, 'EUR': 5.3282, 'INR': 0.06326}
    with mock.patch('converter.api.get_coins_values', return_value=mock_api_result):
        result, status = orchestrator({'price': 300})

        assert result == {'EUR': '56,30\xa0€', 'INR': '₹4,742.33', 'USD': '$61.98'}
        assert status == 200


def test_should_return_error():
    with mock.patch('converter.api.get_coins_values', return_value=None):
        result, status = orchestrator({'price': 300})

        assert result == {'EUR': '56,30\xa0€', 'INR': '₹4,742.33', 'USD': '$61.98'}
        assert status == 500
