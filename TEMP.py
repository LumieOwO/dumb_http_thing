from methods import Put
import json
if __name__ == "__main__":
        data = Put(url='https://demoqa.com/BookStore/v1/Books/', headers={},payload={})
        print(data.response)
        #print(json.loads(data.text)["bpi"]["USD"]["rate_float"])
