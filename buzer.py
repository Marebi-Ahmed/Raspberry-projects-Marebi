import RPi.GPIO as GPIO
import atexit


GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



def switcher(channel): 
    
    if (GPIO.input(2)==True and GPIO.input(3)==True):
        GPIO.output(14, True)
        print("it is ON")
    else:
        GPIO.output(14, False)
        print("it is OFF")

def exitHandler():
    GPIO.cleanup()
    
atexit.register(exitHandler)

GPIO.add_event_detect(2,GPIO.BOTH, callback=switcher) 
GPIO.add_event_detect(3,GPIO.BOTH, callback=switcher)

while(True):
    #GPIO.output(15, False)
    pass
GPIO.cleanup()


