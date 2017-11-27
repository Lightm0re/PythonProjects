"""http://open-notify.org/Open-Notify-API/ISS-Location-N.. - это сервис, которые предоставляет информацию о
геолокации Международной Космической станции.
Ваша задача за показать в какой точке мира находится станция сейчас. """
import urllib.request
import json

x = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
obj = json.loads(x.read())
lat = obj['iss_position']['latitude']
long = obj['iss_position']['longitude']
print('Точка находится по координатам:\n', 'Широта:', lat, 'Долгота:', long)
