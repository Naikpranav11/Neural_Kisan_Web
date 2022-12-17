import requests
r = requests.get('https://scriptsapi.netlify.app/Scripts/test.json')

temperature=r.json()['temperature']['value']
moisture=r.json()['moisture']['value']
pH=r.json()['pH']['value']
Humidity=r.json()['Humidity']['value']
AQI=r.json()['AQI']['value']
print(temperature,moisture,pH,Humidity,AQI)



# {"type":"temperature","value":31,"unit":"°C"}


# {
#     "temperature":
#     {
#         "value":31,
#         "unit":"°C"
#     }
# }