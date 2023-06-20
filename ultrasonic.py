#Raspberry Pi with Python | Arabic number 5

import RPi.GPIO as GPIO
import time
import pickle

Trig_pin=14
Echo_pin=15
Buzzer=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig_pin, GPIO.OUT)
GPIO.setup(Echo_pin, GPIO.IN)
GPIO.setup(Buzzer,GPIO.OUT)

mindistance=50
while (True):
    GPIO.output(Trig_pin, False)
    time.sleep(0.25)
    
    GPIO.output(Trig_pin,True)
    time.sleep(10e-6)  #10 power -6
    GPIO.output(Trig_pin,False)
    
    pulseStart=0.0
    pulseEnd=0.0
    
    while(GPIO.input(Echo_pin)==True):
        pulseStart=time.time()
    while(GPIO.input(Echo_pin)==False):
        pulseEnd=time.time()
    
    duration=pulseStart-pulseEnd
    distance=duration *17150
    print("Distance:{} cm".format(distance))
    if (distance<=mindistance):
        GPIO.ouput(Buzzer, True)
    else:
        GPIO.ouput(Buzzer,False)
    