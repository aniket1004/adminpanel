import requests
import json

URL = 'http://localhost:8000/events/'
def getData(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    
    json_data = json.dumps(data)
    r = requests.get(url =URL,data=json_data)
    data = r.json()
    print(data)

getData()