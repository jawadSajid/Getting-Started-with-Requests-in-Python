import requests
import json
from datetime import datetime

#Error 404
response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(response.status_code)

#API FOUND
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)

#PRINTING JSON DATA RETRIVED
#print(response.json())

#DUMPS() AND LOADS()

#Pythob object to string
text = json.dumps(response.json(),sort_keys=True,indent=4)
#print(text)

#Using an API with Query parameters
parameters = {
    "lat": 40.71, "lon": -74
}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

text = json.dumps(response.json(),sort_keys=True, indent = 4)
#print(text)
#Note that we can do this too: http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74.

pass_time = response.json()['response']
print(pass_time)

risetime = []
duration = []

for i in pass_time:
    print(i)
    time = i['risetime']
    risetime.append(time)
    durations = i['duration']
    duration.append(durations)

print(risetime)
print(duration)

times = []

for rt in risetime:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)