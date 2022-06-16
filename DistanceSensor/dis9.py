import vonage  # Importing the nexmo library
import RPi.GPIO as GPIO
import time

#Connecting to the vonago using API key and API secret
client = vonage.Client(key="f9259294", secret="5ahmSs43om1tVNFb") 
sms = vonage.Sms(client)


# Function to send message
def send_sms():
    # Sending the message
    responseData = sms.send_message(
                                    {
                                        "from": "IOT",
                                         "to": "923172144424",
                                         "text": "Distance Measure",
                                    }
                                    )
    # Checking whether we are successful or we got a error
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")


def DistanceMeasure():
    try:
        GPIO.setmode(GPIO.BCM)
        PIN_TRIGGER = 26
        PIN_ECHO = 20
        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        print("Waiting for sensor to settle")
        time.sleep(2)
        print("Calculating distance")
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()
        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print("Distance:",distance,"cm")
        send_sms()
    
    finally:
        GPIO.cleanup()
        
DistanceMeasure()