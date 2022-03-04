from flask import Flask
from flask import jsonify
from get_api import fetch_data
from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "b890066ddddddddddd444444444444"  # Change this!
jwt = JWTManager(app)

class Flask_app(fetch_data):
    # @app.route("/fetch_market_data", methods=['GET'])

    @app.route("/fetch_market_data", methods=['GET'])
    @jwt_required()
    def get():
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200
        # return (current_user)
        # link = "https://api.bittrex.com/api/v1.1/public/getmarketsummaries"
        # market_data_obj = fetch_data(link)
        # # print(market_data_obj.get_data())
        # return jsonify({'final_result': market_data_obj.get_data()})
#

class Flask_app_marketval(fetch_data):
    @app.route('/getmarketsummary', methods=['GET'])
    def data():
        marketval = request.args.get('market')
        if marketval:#== "btc-ltc":
            link = "https://api.bittrex.com/api/v1.1/public/getmarketsummary?market="+marketval
            market_data_obj = fetch_data(link)
            return jsonify({'final_result': market_data_obj.get_data()})

if __name__ == "__main__":
    app.run(debug=True)