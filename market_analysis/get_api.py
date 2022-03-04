import requests
import  json

class fetch_data():
    def __init__(self,url):
        self.url = url

    def get_data(self):
        response = requests.get(self.url)
        status = response
        result = json.loads(response.text)
        return (result)

# if __name__ == "__main__":
#     link = "https://api.bittrex.com/api/v1.1/public/getmarketsummaries"
#     market_data_obj = fetch_data(link)
#     print(market_data_obj.get_data())
#
