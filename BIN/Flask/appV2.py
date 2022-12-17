import requests

# URL of the API that sends the sensor data
sensor_data_url = 'http://example.com/sensor-data'

# URL of the API that controls the devices
device_control_url = 'http://example.com/device-control'

# Threshold values for the sensor data
temperature_threshold = 25  # degrees Celsius
humidity_threshold = 50  # percent
light_threshold = 500  # lux
pressure_threshold = 1000  # pascals

while True:
  print('Hello')
  # Get the sensor data from the API
  sensor_data = requests.get(sensor_data_url).json()

  # Process the sensor data and control the devices as needed
  if sensor_data['temperature'] > temperature_threshold:
    requests.post(device_control_url, json={'device': 'air conditioning', 'action': 'turn on'})
  else:
    requests.post(device_control_url, json={'device': 'air conditioning', 'action': 'turn off'})

  if sensor_data['humidity'] > humidity_threshold:
    requests.post(device_control_url, json={'device': 'humidifier', 'action': 'turn on'})
  else:
    requests.post(device_control_url, json={'device': 'humidifier', 'action': 'turn off'})

  if sensor_data['light'] > light_threshold:
    requests.post(device_control_url, json={'device': 'lights', 'action': 'turn on'})
  else:
    requests.post(device_control_url, json={'device': 'lights', 'action': 'turn off'})

  if sensor_data['pressure'] > pressure_threshold:
    requests.post(device_control_url, json={'device': 'pump', 'action': 'increase pressure'})
  else:
    requests.post(device_control_url, json={'device': 'pump', 'action': 'decrease pressure'})
