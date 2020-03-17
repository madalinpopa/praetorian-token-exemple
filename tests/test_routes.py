# coding: utf-8

# tests/test_routes.py



def test_smoke(client):
    rv = client.get('/')
    assert rv.status_code == 200