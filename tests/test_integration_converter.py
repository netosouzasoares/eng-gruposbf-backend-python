from app import app
import json


def test_converter_route():
    response = app.test_client().post('/converter', data=json.dumps(dict(price=200)), content_type='application/json')

    assert response.status_code == 200


def test_healthcheck_route():
    response = app.test_client().get('/healthcheck')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'app running'
