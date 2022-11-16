import json
import requests 

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=778ac911e271c26cfb46581a2cbc2c90' % zip)
data=r.json()

print(data['weather'][0]['description'])