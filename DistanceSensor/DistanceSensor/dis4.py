from gpiozero import DistanceSensor

# The default range threshold is 0.3m.
#This can be configured when the sensor is initiated:
dis = DistanceSensor(echo=17, trigger=4, threshold_distance=0.5)

while True:
    print("%.3f"%dis.distance, ' cm')