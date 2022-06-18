import Adafruit_DHT
from pushbullet import Pushbullet

pb = Pushbullet("o.t8XGOI0l8fEuYdqerwYs0vAHtQ2kCkMu") # your access token
print(pb.devices)
sensor=Adafruit_DHT.DHT11
gpio=17
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    dev = pb.get_device('INFINIX MOBILITY LIMITED Infinix X650B')
    push = dev.push_note("Sensor Alert!","Room Temperature is: {0:0.1f}*C \nHumidity is: {1:0.1f}%".format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
