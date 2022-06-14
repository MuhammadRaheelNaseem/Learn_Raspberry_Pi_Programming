import RPi.GPIO as GPIO 
import time

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail= MIMEMultipart()
server = smtplib.SMTP('smtp.gmail.com',587) #SMTP Server and Port Number
server.starttls() #Server Starting
sender = ' ' # Type your own email ID
senpass = ' ' # Enter the password associated with the email
receiver = 'mrahilnasim@gmail.com' # Receiver's Email ID
server.login(sender,senpass) #Authentication Point


GPIO.setmode(GPIO.BOARD)#Numbering the GPIO pin
GPIO.setwarnings(False)
GPIO_TRIGGER = 24
GPIO_ECHO = 23
pulse_start=0
pulse_end=0
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) #GPIO Mapping 
GPIO.setup(GPIO_ECHO,GPIO.IN)

while True:

    GPIO.output(GPIO_TRIGGER, True)
     # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because reflected or echo signal
    distance = (TimeElapsed * 34300) / 2
    print(distance)
    if distance < 50 : #Only sends mail when sensor reads object from less than 50 cm
        mail['From']='Home Automation Systems'
        mail['To'] = receiver
        mail['Subject']='Sensor Data – Alert'
        body='Object detected'
        mail.attach(MIMEText(body,'plain')) 
        msg=mail.as_string()
        server.sendmail(sender,receiver,msg)
        print('Mail Sent')
    time.sleep(5)   #The sensor checks the object in every 5 seconds
GPIO.cleanup()