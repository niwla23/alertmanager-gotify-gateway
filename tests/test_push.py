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


def test_multi_firing(client: FlaskClient):
    client.post('/push', json={
        'receiver': 'managers-email',
        'status': 'firing',
        'alerts': [
            {
                'status': 'firing',
                'labels': {
                    'alertname': 'http_probe_failed',
                    'instance': 'http://192.168.178.33:5000',
                    'job': 'ping',
                    'monitor': 'my-project',
                    'severity': 'page'
                },
                'annotations': {
                    'description': 'http://192.168.178.33:5000 of job ping has been down for more than 3 minutes.',
                    'summary': 'test_multi_firing 1'
                },
                'startsAt': '2022-02-06T22:50:16.656Z',
                'endsAt': '0001-01-01T00:00:00Z',
                'generatorURL': 'http://868e591da566:9090/graph?g0.expr=probe_success%7Bjob%3D%22ping%22%7D+%3D%3D+0&g0.tab=1',
                'fingerprint': '921ff287cafdcd61'
            },
            {
                'status': 'firing',
                'labels': {
                    'alertname': 'http_probe_failed',
                    'instance': 'http://smartdashboard.sweet',
                    'job': 'ping',
                    'monitor': 'my-project',
                    'severity': 'page'
                },
                'annotations': {
                    'description': 'http://smartdashboard.sweet of job ping has been down for more than 3 minutes.',
                    'summary': 'test_multi_firing 2'
                },
                'startsAt': '2022-02-06T22:50:16.656Z',
                'endsAt': '0001-01-01T00:00:00Z',
                'generatorURL': 'http://868e591da566:9090/graph?g0.expr=probe_success%7Bjob%3D%22ping%22%7D+%3D%3D+0&g0.tab=1',
                'fingerprint': '968ff408c62f5952'
            }
        ],
        'groupLabels': {
            'alertname': 'http_probe_failed'
        },
        'commonLabels': {
            'alertname': 'http_probe_failed',
            'job': 'ping',
            'monitor': 'my-project',
            'severity': 'page'
        },
        'commonAnnotations': {},
        'externalURL': 'http://2ac8f3e63dd8:9093',
        'version': '4',
        'groupKey': '{}:{alertname="http_probe_failed"}',
        'truncatedAlerts': 0
    })

    x = input("did you receive **two** push messages? (yes/no)")
    assert x.lower() == "yes"
