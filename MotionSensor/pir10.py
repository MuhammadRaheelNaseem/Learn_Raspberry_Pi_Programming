import vonage  # Importing the nexmo library
import RPi.GPIO as GPIO
from time import sleep

sensor_pin = 4        # Initialized GPIO 17 for motion sensor
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)         # Declared GPIO 17 as input pin

# Connecting to the vonago using API key and API secret
client = vonage.Client(key="f9259294", secret="5ahmSs43om1tVNFb") 
sms = vonage.Sms(client)


# Function to send message
def send_sms():
    # Sending the message
    responseData = sms.send_message(
                                    {
                                        "from": "IOT",
                                         "to": "923172144424",
                                         "text": "Motion Detected!",
                                    }
                                    )
    # Checking whether we are successful or we got a error
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

for i in range(3):
    try:
        # Reading the motion sensor pin state
        pin_state = GPIO.input(sensor_pin)
        if pin_state==0:                 #When output from motion sensor is LOW
            print("Body Not Detected",pin_state)
            sleep(0.1)

        elif pin_state==1:               #When output from motion sensor is HIGH
            print("Body Detected",pin_state)
            send_sms()
            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleaup()
    sleep(2)