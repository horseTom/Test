from unittest.mock import MagicMock
import pytest
import requests

@pytest.fixture(autouse=True)
def mock_request(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    #monkeypatch.delattr("requests.sessions.Session.request")
    def mock(*args, **kwargs):
        print("mock")
        print(args)
        print(kwargs)
        return "mock"
    monkeypatch.setattr(requests.sessions.Session, "send", mock)

def test_post():
    print(requests.request("get", "http://www.baidu.com"))
    print(requests.post("http://www.baidu.com"))

def test_mock():
    requests.request = MagicMock(return_value="mock")
    print(requests.request("get", "http://www/baidu.com"))