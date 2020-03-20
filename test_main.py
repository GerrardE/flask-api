'''
Tests for flask-api
'''
import os
import json
import pytest
import main


@pytest.fixture
def client():
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client


def test_home(client):
    response = client.get('/')
    response_copy = {
        "status": 200,
        "message": "You successfully hit the /home route"
    }
    assert response.status_code == 200
    assert response.json == response_copy


def test_data(client):
    body = {
        "test": "test_body"
    }
    response_copy = {
        "status": 200,
        "message": "You successfully hit the /data route"
    }
    response = client.post('/data',
                           data=body,
                           content_type='application/json')
    assert response.status_code == 200
    response_data = response.json
    assert response_data == response_copy
