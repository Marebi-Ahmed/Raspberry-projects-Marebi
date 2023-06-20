import tkinter
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led_pin=21
GPIO.setup(led_pin,GPIO.OUT)
pwm1=GPIO.PWM(led_pin,1000)  #frequency
pwm1.start(0) #duty cycle
#GPIO.setup(20,GPIO.OUT)

isCodeRunning=True
bt_state=False
def exit_handler():
    global isCodeRunning,window
    window.destroy()
    isCodeRunning=False
    print("done")

def btonoffHandler():
    global bt_state,slider
    bt_state=not bt_state
    if (bt_state==False):
        btstr.set("OFF")
        slider.configure(state="disabled")
    else:
        btstr.set("ON")
        slider.configure(state="active")
        
    
    

window=tkinter.Tk() #to create GUI
window.title("PWM signal")
window.geometry("300x100")
#this command is used close the GUI, and call a function that we use to exit the main program loop
window.protocol("WM_DELETE_WINDOW",exit_handler) 


btstr=tkinter.StringVar()
btstr.set("OFF")
btn=tkinter.Button(window,textvariable=btstr,command=btonoffHandler)
slider=tkinter.Scale(window,from_=0,to=100, orient=tkinter.HORIZONTAL)
slider.configure(state="disabled")

slVal=tkinter.StringVar()
label1=tkinter.Label(window,textvariable=slVal,width=100)
slVal.set("Slider Value: OFF")

btn.pack()
slider.pack()
label1.pack()
#this command a loop for GUI, but if we have a program main loop we just use the command window.update()
#window.mainloop()

while(isCodeRunning):
    
    sliderValue=slider.get()
    if (bt_state==True):
        sliderValue=slider.get()
        pwm1.ChangeDutyCycle(sliderValue)
        #GPIO.output(20,True)
        slVal.set("Slider Value:" +str(sliderValue))
        print(sliderValue)
    else:
        pwm1.ChangeDutyCycle(0)
        #GPIO.output(20,False)
        slVal.set("Slider Value: OFF")
        print("it is off")
        
    window.update()
    time.sleep(0.25)
GPIO.cleanup()
