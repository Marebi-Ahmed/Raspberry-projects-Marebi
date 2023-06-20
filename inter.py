import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#interrupt return function, this is called when iterrupt is on
def test(switch): #switch is a variable returning from interrupt
    
    if (GPIO.input(switch)==True):
        GPIO.output(15, True)
        print("it is ON")
    else:
        GPIO.output(15, False)
        print("it is OFF")

GPIO.add_event_detect(2,GPIO.BOTH, callback=test) #interrupt

while(True):
    #GPIO.output(15, False)
    pass
GPIO.cleanup()