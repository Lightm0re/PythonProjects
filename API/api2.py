"""https://pokeapi.co/ - ПОКЕМОНЫ!!! Тут собрана вся информация о покемонах. Необходимо получить номер покемона и
выдать краткую информацию о нем. """
import urllib.request
import json
headers = {}
n = input('Введите номер покемона')
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
x = urllib.request.Request('http://pokeapi.co/api/v2/pokemon/' + n, headers=headers)
resp = urllib.request.urlopen(x)
obj = json.loads(resp.read())
print(obj)

