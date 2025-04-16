from Lib.test.test_future_stmt.import_nested_scope_twice import result

import requests

def hello_webdata() -> None:
    print("Hello Webdata")

def get_data() -> str:
    url = 'https://data.townofcary.org/api/v2/catalog/datasets/rdu-weather-history'

    print(requests.get(url))

    if requests.get(url).status_code == 200:
        print("OK")
        response = requests.get(url)
        print(response.json())
    else:
        raise ConnectionError("get_data failed")

    return 'gugus'