import requests
import json

class City:
    def __init__(self, Name, Temperature):
        self.Name = Name
        self.Temperature = Temperature

cities = ['London', 'Sydney', 'Tokyo', 'Madrid','Addis Ababa']
all_cities = []
myAPIKey = 'd76dc1c3895fd014e06ab642c7970db6'
for city_name in cities:
    my_url = 'https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}'.format(myAPIKey, city_name)
    all_cities.append(City(city_name, json.loads(requests.get(my_url).text)['main']['temp'] - 273.15))
all_cities.sort(key=lambda x: x.Temperature, reverse=False)
for ac in all_cities:
    print "the temperature in {0} is {1} Degrees celsius".format(ac.Name, ac.Temperature)
pass