import requests
import time
import json
import collections

cities = ['London', 'Paris', 'Sydney', 'Addis Ababa']
city_temps = {}

for city in cities:
    url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={APIKEY}'.format(
        APIKEY='36deadf11833327147c028f524c3bb99', city=city)
    resp = requests.get(url)
    content = json.loads(resp.content)
    temperature = content['main']['temp']
    city_temps.update({
        city: temperature
    })

sorted_dict = collections.OrderedDict(city_temps)
for key,value in city_temps.iteritems():
    print '{0} : {1}'.format(key , value-273.15)
pass


