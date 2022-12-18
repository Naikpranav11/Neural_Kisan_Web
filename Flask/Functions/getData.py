import requests
import random
# r = requests.get('https://scriptsapi.netlify.app/Scripts/test.json')

# temperature=r.json()['temperature']['value']
# moisture=r.json()['moisture']['value']
# pH=r.json()['pH']['value']
# Humidity=r.json()['Humidity']['value']
# AQI=r.json()['AQI']['value']
# print(temperature,moisture,pH,Humidity,AQI)

def APIJSON(URL):
    r = requests.get(URL)


    # data=f'{"temperature":{"value":31,"unit":"°C"},"moisture":{"value":54,"unit":"°C"},"pH":{"value":5,"unit":"°C"},"Humidity":{"value":39,"unit":"°C"},"AQI":{"value":100,"unit":"°C"}}'
    # r.json()['temperature']['value']=random.randint()
    # r.json()['moisture']['value']=random.randint()
    # r.json()['pH']['value']=random.randint()
    # r.json()['Humidity']['value']=random.randint()
    # r.json()['AQI']['value']=random.randint()

    return(r.json())
    # return(data)



def Instructions(param,cutoff):
    # if(param):
    if(int(APIJSON('https://scriptsapi.netlify.app/Scripts/test.json')[param]['value'])>cutoff):
        return 'Cool System Down'
    else:
        return 'Do Nothing'