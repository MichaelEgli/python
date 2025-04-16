from typing import Any

import requests


from requests import Response


def hello_webdata() -> None:
    print("Hello Webdata")

def get_data() -> Response | Any:
    url = 'https://data.townofcary.org/api/v2/catalog/datasets/rdu-weather-history'

    print(requests.get(url))


    if requests.get(url).status_code == 200:
        print("OK")
        response = requests.get(url)
        print(response.json())
        return response
    else:
        raise ConnectionError("get_data failed")

