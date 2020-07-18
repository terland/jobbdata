import requests
import json

bearercode = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwdWJsaWMudG9rZW4udjFAbmF2Lm5vIiwiYXVkIjoiZmVlZC1hcGktdjEiLCJpc3MiOiJuYXYubm8iLCJpYXQiOjE1NTc0NzM0MjJ9.jNGlLUF9HxoHo5JrQNMkweLj_91bgk97ZebLdfx3_UQ'

headers = {'authorization': 'Bearer ' + bearercode}
endpoint = 'https://arbeidsplassen.nav.no/public-feed/api/v1/ads'
data = {}

r = requests.get(endpoint,data = data,headers = headers)
data = r.json()
print(data['content'][0]['description'])