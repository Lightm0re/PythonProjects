"""http://www.recipepuppy.com/about/api/ - это сервис для получения рецептов. Задача простая: передаем список
продуктов, получаем рецепты для этого списка продуктов """
import urllib.request
import json
headers = {}
n = input('Введите ингридиенты (через запятую)')
n.replace(',', '%2C+')
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
x = urllib.request.Request('http://www.recipepuppy.com/api/?i=' + n, headers=headers)
resp = urllib.request.urlopen(x)
obj = json.loads(resp.read())
print(obj)
