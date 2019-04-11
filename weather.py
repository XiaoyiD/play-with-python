# get the weather info of a specific city

CITY_CODE = '101020100' # City code of 上海
LINK = 'http://www.weather.com.cn/data/sk/' + CITY_CODE + '.html'

import requests
r = requests.get(LINK)
r.encoding = 'utf-8'
print(r.json()['weatherinfo']['city'], r.json()['weatherinfo']['WD'], r.json()['weatherinfo']['temp'])
