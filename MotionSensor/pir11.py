import smtplib, ssl
from gpiozero import MotionSensor

pir = MotionSensor(4) # gpio pin number


def mail():
    global psd
    print("Motion Detected!")
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "johnmalton734@gmail.com"
    password = "Enter Your Password"
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be comitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be comitted
        server.login(sender_email, password)
        print("Successfully login") 
        subject="mail from Raspberry Pi "
        body="Motion Has Been Detected!"
        message="Subject: {}\n\n{}".format(subject,body)
        address=['mrahilnasim@gmail.com']
        server.sendmail("johnmalton734",address,message)
        print('Mail send successfully')
    except Exception:
        print("Login Failed")
        print("Try to enter correct password")
    finally:
        print('Server Has Been Successfully Close')
        server.quit() 

def no_mail():
    print("No Motion Detected!")

pir.wait_for_motion()
mail()
print("!!!!!!!!!!")
pir.wait_for_no_motion()
no_mail()
