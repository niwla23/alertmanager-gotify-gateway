import pytest
import unittest
from gateway import app
from flask.testing import FlaskClient


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_firing(client: FlaskClient):
    client.post('/push', json={
        'receiver': 'managers-email',
        'status': 'firing',
        'alerts': [
            {
                'status': 'firing',
                'labels': {
                  'alertname': 'testing',
                  'gateway': '192.168.178.1',
                  'instance': 'fritzbox-exporter:9133',
                  'job': 'fritzbox',
                  'monitor': 'my-project',
                  'severity': 'page'
                },
                'annotations': {
                    'description': 'this is a test alert',
                    'summary': 'Test alert'
                },
                'startsAt': '2022-02-06T17:32:16.656Z',
                'endsAt': '0001-01-01T00:00:00Z',
                'generatorURL': 'http://868e591da566:9090/graph?g0.expr=gateway_wan_connection_uptime_seconds+%3E+3&g0.tab=1',
                'fingerprint': 'f62a7d6619c829cc'
            }
        ],
        'groupLabels': {
            'alertname': 'testing'
        },
        'commonLabels': {
            'alertname': 'testing',
            'gateway': '192.168.178.1',
            'instance': 'fritzbox-exporter:9133',
            'job': 'fritzbox',
            'monitor': 'my-project',
            'severity': 'page'
        },
        'commonAnnotations': {
            'description': 'this is a test alert',
            'summary': 'Test alert'
        },
        'externalURL': 'http://2ac8f3e63dd8:9093',
        'version': '4',
        'groupKey': '{}:{alertname="testing"}',
        'truncatedAlerts': 0
    })

    x = input("did you receive a push message? (yes/no)")
    assert x.lower() == "yes"