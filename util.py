import requests

def request(base_url, *args):
    url = base_url + "?"
    for arg in args:
        url = url + arg + "&"
    return requests.get(url).json()
     

