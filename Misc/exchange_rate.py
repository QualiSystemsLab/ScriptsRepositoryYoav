import requests
import json

qqq = requests.get('https://api.exchangeratesapi.io/2016-01-12?base=ILS&symbols=ILS,GBP')
a = json.loads(qqq.content)
pass