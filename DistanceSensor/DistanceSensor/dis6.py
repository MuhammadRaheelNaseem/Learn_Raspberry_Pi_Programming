from gpiozero import DistanceSensor
from time import sleep
import requests

server_url = 'http://localhost:9090'
threshold_distance = 0.9

#sensor = DistanceSensor(echo=18, trigger=17, threshold_distance=threshold_distance)
sensor = DistanceSensor(echo=18, trigger=17)

while True:
    #sensor.wait_for_in_range()
    r = requests.post(server_url, json={'distance': (sensor.distance * 100)});
    if r.status_code == 200:
        print('Pushed distance of ', sensor.distance * 100, ' to the server')
    else:
        print('Failed to push distance to server')
    print('Detected Distance: ', sensor.distance * 100)
        sleep(1)