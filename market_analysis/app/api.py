from flask import Flask
from flask import jsonify
from get_api import fetch_data
from flask import request
# from dotenv import load_dotenv
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import os
# load_dotenv()
# usr = os.getenv("username")
# pwd = os.getenv("password")

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

##login api for user and password
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test_username" or password != "test_123":
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


##get request to find all data
class Flask_app(fetch_data):
    @app.route("/fetch_market_data", methods=['GET'])
    @jwt_required()
    def get(self):
        link = "https://api.bittrex.com/api/v1.1/public/getmarketsummaries"
        market_data_obj = fetch_data(link)
        return jsonify({'final_result': market_data_obj.get_data()})


###get request to find data with query parametet of market data
# # http://127.0.0.1:5000/getmarketsummary?market=btc-ltc
class Flask_app_marketval(fetch_data):
    @app.route("/getmarketsummary", methods=["GET"])
    @jwt_required()
    def protected(self):
        marketval = request.args.get('market')
        if marketval:#== "btc-ltc":
            link = "https://api.bittrex.com/api/v1.1/public/getmarketsummary?market="+marketval
            market_data_obj = fetch_data(link)
            return jsonify({'final_result': market_data_obj.get_data()})
        if not marketval:
            try:
                raise ValueError('market value unavailable')
            except ValueError as e:
                print(e)



if __name__ == "__main__":
    app.run(debug=True)