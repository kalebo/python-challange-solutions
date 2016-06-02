import requests
import re

current_nothing = "12345"

PROTO = "http://"
DOMAIN = "www.pythonchallenge.com"
PATH = "/pc/def/linkedlist.php"

url = PROTO + DOMAIN + PATH 


def fetch_nothing(current_nothing):
    payload = {'nothing': current_nothing}
    r = requests.get(url, params=payload)
    print(r.text)
    nothing = re.search("next nothing is ([0-9]+)", r.text)
    if nothing == None:
        return str(int(current_nothing)/2)
    else:
        return nothing.group(1)


new_nothing = fetch_nothing(current_nothing)

for i in range(400):
    new_nothing = fetch_nothing(new_nothing)


