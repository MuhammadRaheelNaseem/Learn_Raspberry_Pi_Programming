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
@app.route("//")
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
