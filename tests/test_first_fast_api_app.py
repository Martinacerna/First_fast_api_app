from first_fast_api_app import __version__
from first_fast_api_app.app import app
from fastapi import FastAPI
from fastapi.testclient import TestClient
import requests

client = TestClient(app)


def test_version():
    assert __version__ == "0.1.0"


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}
