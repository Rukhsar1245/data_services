import requests
import  json

class fetch_data():
    def __init__(self,url):
        self.url = url

    def get_data(self):
        try:
            response = requests.get(self.url)
            status = response
            # 404
            # JSONDecodeError("Expecting value", s, err.value)
            print(response.text)
            result = json.loads(response.text)
            response.raise_for_status()
            return (result)
        except ValueError as e:  # includes simplejson.decoder.JSONDecodeError
            print(e,'Decoding JSON has failed')
        except requests.exceptions.HTTPError as e:
            print(e.response.text)
        except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))
        except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            print(str(e))
        except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
        except KeyboardInterrupt:
            print("Someone closed the program")
        except Exception as exc:
            print ("other error found")
            print(type(exc), str(exc))

if __name__ == "__main__":
    link = "https://api.bittrex.com/api/v1.1/public/getmarketsummaries"
    market_data_obj = fetch_data(link)
    print(market_data_obj.get_data())

