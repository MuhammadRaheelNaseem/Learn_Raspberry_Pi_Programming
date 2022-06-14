<h1 class='jumbotron alert-info'>6.) DHT11 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Digital Humidity and Temperature) </h1>

The DHT11 is an ultra low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and thermistor to measure the surrounding air, and spits out a digital signal on the data pin (no analog input pins needed), with no onboard power supply.
![image](https://user-images.githubusercontent.com/63813881/173555815-a3a951f8-c390-4e47-a5e2-61b4d43c7cff.png)
![image](https://user-images.githubusercontent.com/63813881/173555839-a11fb58a-0ff2-4f13-8deb-f55574d25b4f.png)

# `Circuit Diagram:`

![image](https://user-images.githubusercontent.com/63813881/173555867-e211b903-70e5-40ee-b959-ba49d9cf90b8.png)

# `Code: 1`
<pre>
<h2>pip install Adafruit-DHT </h2>
<!-- import Adafruit_DHT 
sensor = Adafruit_DHT.DHT11 pin = 4 
while True:
    humidity , temperature = Adafruit DHT . read_retry ( sensor , pin ) 
    print ( " Temp = ( 0 : 0.1f ) C Humidity = ( 1 : 0.1f )" % . format ( temperature , humidity))
     -->
import Adafruit_DHT
 
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
gpio=17
 
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
 
# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.
if humidity is not None and temperature is not None:
  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
  print('Failed to get reading. Try again!')

</pre>

# `Code: 2`
<pre>
import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 14)
# read() method, which will return DHT11 Result object with actual values and error code.
result = instance.read()

if result.is_valid():
    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
</pre>

# `Code: 3`
<pre>
import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=21)

while True:
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)

    time.sleep(1)
</pre>

# `Code: 4`
<pre>
# pip3  install Adafruit_Python_DHT
# pip3 install Flask
# pip3 install Flask-RESTful

try:
    from flask import Flask
    from flask_restful import Resource,Api
    from flask_restful import reqparse
    from flask import request
    import time
    import datetime
    import json
    import Adafruit_DHT
    print("All modules loaded ")
except Exception as e:
    print("Error: {}".format(e))

app = Flask(__name__)
api = Api(app)

pin = 17
sensor = Adafruit_DHT.DHT11


class Sensors(object):

    def __init__(self):
        pass

    def get(self):

        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            return{
                'Temperature':temperature,
                "humidity":humidity
            }


class Controller(Resource):
    def __init__(self):
        pass

    def get(self):
        helper = Sensors()
        return helper.get()


api.add_resource(Controller, "/")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
</pre>

## `want to see in python command line`
<pre>
import requests

url = "IP address which provide by flask"
read = requests.get(url)
print(read.json())

# `Code: 5`
<pre>
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
</pre>

# `Code: 6`
<code>
from pushbullet import Pushbullet
import RPi.GPIO as GPIO
import dht11
import time

pb = Pushbullet("o.t8XGOI0l8fEuYdqerwYs0vAHtQ2kCkMu") # your access token
print(pb.devices)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

instance = dht11.DHT11(pin=21)

while True:
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
        dev = pb.get_device('INFINIX MOBILITY LIMITED Infinix X650B')
        push = dev.push_note("Sensor Alert!","Room Temperature is: {0:0.1f}*C \nHumidity is:{1:0.1f}%".format(result.temperature, result.humidity))
    time.sleep(1)
</code>

# `goto this link` https://thingspeak.com/login `Click create one then fill all fields`

![image](https://user-images.githubusercontent.com/63813881/173555964-20010d7e-4d02-4fd3-866e-3668b74d8055.png)

# `Like this then press continue`
![image](https://user-images.githubusercontent.com/63813881/173556025-eac6c757-aefb-4cf3-889b-172543d2c6ae.png)
# `Click My Channel`
![image](https://user-images.githubusercontent.com/63813881/173556072-68d63227-28a2-41bd-8383-500beeab444a.png)
`We will define the channels by entering the a proper name, description, and up to 8 fields can be used to name the parameter. For the Field 1 and Field 2 we have named Temperature and humidity. These field values ​​that you set can be modified later. These values will be in Degree Centigrade and Relative Humidity in %. Once you update the name, click on Save.`
![image](https://user-images.githubusercontent.com/63813881/173556098-51c76d37-e8be-4721-a1d7-53168a5348be.png)
`Once you have saved the channel, you will be automatically redirected to the “Private View” tab. Here the mapped fields are shown as a diagram. You will find the “Channel ID” (we will need it later). Below You will also see API Keys option.`
![image](https://user-images.githubusercontent.com/63813881/173556137-4537918b-9680-47ef-ae7a-0ed1579803e3.png)
`Later, click on the “API Keys” tab. The two values ​​of “Write API key” and “Read API key” are equally necessary for us to write or retrieve data. Copy these keys and keep it safe as we need to put it in the code.`
![image](https://user-images.githubusercontent.com/63813881/173556171-4681026e-ac08-4264-91c3-32575a15a225.png)
## `sudo pip install thingspeak`

# `Code: 7`
<pre>
import thingspeak
import time
import Adafruit_DHT

channel_id = # put here the ID of the channel you created before
write_key = # update the "WRITE KEY" in string form

pin = 4
sensor = Adafruit_DHT.DHT11

def measure(channel):
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print('Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity))
        else:
            print('Did not receive any reading from sensor. Please check!')
        # update the value
        response = channel.update({'field1': temperature, 'field2': humidity})
    except:
           print("connection failure")

if __name__ == "__main__":
        channel = thingspeak.Channel(id=channel_id, write_key=write_key)
        while True:
            measure(channel)
        #free account has a limitation of 15sec between the updates
            time.sleep(15)
</pre>

# `Code: 8`
### `Raspberry Pi Flask Web Server with DHT11`
<pre>
from flask import Flask, render_template
import RPi.GPIO as GPIO
import Adafruit_DHT as dht
 
app = Flask(__name__)
 
GPIO.setmode(GPIO.BCM)
led1 = 21 
led2 = 20
DHT11_pin = 23
 
# Set each pin as an output and make it low:
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
 
@app.route("/")
 
def main():
   return render_template('main.html')
 
# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<pin>/<action>")
def action(pin, action):
   temperature = ''
   humidity = ''
   if pin == "pin1" and action == "on":
      GPIO.output(led1, GPIO.HIGH)
    
   if pin == "pin1" and action == "off":
      GPIO.output(led1, GPIO.LOW)
    
   if pin == "pin2" and action == "on":
      GPIO.output(led2, GPIO.HIGH)
    
   if pin == "pin2" and action == "off":
      GPIO.output(led2, GPIO.LOW)
 
   if pin == "dhtpin" and action == "get":
      humi, temp = dht.read_retry(dht.DHT11, DHT11_pin)  # Reading humidity and temperature
      humi = '{0:0.1f}' .format(humi)
      temp = '{0:0.1f}' .format(temp)
      temperature = 'Temperature: ' + temp 
      humidity =  'Humidity: ' + humi
 
   templateData = {
   'temperature' : temperature,
   'humidity' : humidity
   }
 
   return render_template('main.html', **templateData)
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
</pre>

# `Paste this code in templates folder ↓
<!-- <html>
<head>
<title>Raspberry Pi Webserver</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
<meta name="viewport" content = "width=device-width, initial-scale=1.0">

</head>
<style>
.row {
display: flex;
justify-content: space-between;
}
.column {
flex: 33%;
padding: 10px;
}
</style>
<body style="background: white">
<h1 align="center"; style="color: navy"><u>Raspberry Pi Webserver</u></h1>
<br>
<br>
<h2 align="center"> Click below to get Temperature & Humidity data </h2>
<p align="center"><button><a href="/dhtpin/get" style="color: teal"> Click Here </a></button></p>

<h4 align="center"; style="color: red"> {{ temperature }} &deg;C</h4>
<h4 align="center"; style="color: red"> {{ humidity }} RH</h4>
<br>
<div align="center">
<div class="column">
<h3 style="color: blue">Device 1
<button>
<a href="/pin1/on" style="color: green"> ON</a>
</button>
<button>
<a href="/pin1/off" style="color: red"> OFF</a>
</button>
</h3>
</div>
<div class="column">
<h3 style="color: blue">Device 2
<button>
<a href="/pin2/on" style="color: green"> ON</a>
</button>
<button>
<a href="/pin2/off" style="color: red"> OFF</a>
</button>
</h3>
</div>
</div>
</body>
</html>
 -->
