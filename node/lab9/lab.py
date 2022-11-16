import json
import requests 



r = requests.get('http://localhost:3000/')
data=r.json()

print(data) 
