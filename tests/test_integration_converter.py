from app import app
import json


def test_converter_should_return_sucess():
    response = app.test_client().post('/converter', data=json.dumps(dict(price=200)), content_type='application/json')

    assert response.status_code == 200


def test_healthcheck_should_return_200():
    response = app.test_client().get('/healthcheck')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'app running'


def test_converter_should_return_bad_request_if_price_is_zero():
    response = app.test_client().post('/converter', data=json.dumps(dict(price=0)), content_type='application/json')

    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Field price is invalid'


def test_converter_should_return_bad_request_if_price_is_negative():
    response = app.test_client().post('/converter', data=json.dumps(dict(price=-1)), content_type='application/json')

    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Field price is invalid'


def test_converter_should_return_bad_request_if_price_is_string():
    response = app.test_client().post('/converter', data=json.dumps(dict(price="200")), content_type='application/json')

    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Field price is invalid'


def test_converter_should_return_bad_request_if_body_is_invalid():
    response = app.test_client().post('/converter', data=json.dumps({}), content_type='application/json')

    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Field price is required on body'
