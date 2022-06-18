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
    app.run(host="127.0.0.1")
    

# If you want see reading in terminal when flask code is running 
# How to fatch reading in terminal either flask code or server is running 
# import requests
# url = "127.0.0.1"
# read = requests.get(url)
# print(read.json())
