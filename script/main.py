import requests
import json
from bs4 import BeautifulSoup as bs
import webbrowser

bearercode = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwdWJsaWMudG9rZW4udjFAbmF2Lm5vIiwiYXVkIjoiZmVlZC1hcGktdjEiLCJpc3MiOiJuYXYubm8iLCJpYXQiOjE1NTc0NzM0MjJ9.jNGlLUF9HxoHo5JrQNMkweLj_91bgk97ZebLdfx3_UQ'

headers = {'authorization': 'Bearer ' + bearercode}
endpoint = 'https://arbeidsplassen.nav.no/public-feed/api/v1/ads'
data = {}

def get_jobs(data = {}):
    r = requests.get(endpoint,data = data,headers = headers)
    return(r.json())


data = get_jobs()
data = data['content'][0]

pretty = json.dumps(data, indent=4, sort_keys=True)

with open('files/description.html', 'a') as f:
    description = data['description']
    f.write(description)
    
webbrowser.open_new_tab('files/description.html')
