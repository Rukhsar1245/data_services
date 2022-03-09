import pytest
import requests
import json
from flask import Flask
from flask import jsonify

@pytest.fixture(scope="function")
def app():
      #def get():
          app = Flask(__name__)
          @app.route("/protected", methods=["GET"])
          def access_protected():
              link = "https://api.bittrex.com/api/v1.1/public/getmarketsummaries"
              mar = requests.get(link)
              return jsonify(response=mar.status_code)
          return app

def test_successful_operation(app):
    test_client = app.test_client()
    response = test_client.get("/protected")
    assert response.get_json() == {"response":200 }

"""def test_failed_operations(app):
    test_client = app.test_client()
    response = test_client.get("/protected")

    assert response.status_code == 401
    assert response.get_json() == {"msg": "Missing Authorization Header"}

    assert response.status_code == 422
    assert response.get_json() == {"msg": "Only non-refresh tokens are allowed"}"""

@pytest.fixture(scope="function")
def app1():
    app1 = Flask(__name__)
    @app1.route("/querydata", methods=["GET"])
    def access_marketwith_query():
        q = "btc-ltc"
        link = "https://api.bittrex.com/api/v1.1/public/getmarketsummary?market="+q
        mar = requests.get(link)
        return jsonify(response=mar.status_code)
    return app1

def test_successful_operation(app1):
        test_client = app1.test_client()
        response = test_client.get("/querydata")
        assert response.get_json() == {"response": 200}

"""def test_failed_operations(app1):
        test_client = app1.test_client()
        response = test_client.get("/querydata")
        assert response.status_code == 401
        assert response.get_json() == {"msg": "Missing Authorization Header"}
        assert type(response.get_json()[0]) is dict"""
#


