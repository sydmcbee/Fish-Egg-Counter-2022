import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
#SetupSwitch
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#Toggle Mode
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#Increment
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#Increment Line
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#Toggle Switch
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback2, bouncetime=30) # Setup event on pin 10 rising edge
def incDgtFnc(channel):
    global incDgt
    incDgt = 1

def incLnFnc(channel):
    global incLine
    incLine = 1


GPIO.add_event_detect(12,GPIO.RISING,callback=incDgtFnc, bouncetime =300) # Setup event on pin 10 rising edge
GPIO.add_event_detect(16,GPIO.RISING,callback=incLnFnc, bouncetime = 300) # Setup event on pin 10 rising edge


##########
#some code to pull count & batch & batchsize
#Also does ErrorHandling if It remembers these things
try:
    count >= 0
#pull from image data?   ***************
except: 
    count = 0
try:
    batchsize >= 0
except: 
    batchsize = 0
try:
    batch >= 1
#ditto here               **************
except: 
    batch = 0
#########

strtmenu=8
mode=10
nextline=12
addline=16
try:
    n = 1


except:
    print("Button Setup Failed")
#Add Code to say button setup Failed *************

########
global incDgt
global incLine
incDgt = 0
incLine = 0
print("boot")
while true
    while GPIO.input(strtmenu) == GPIO.HIGH:
        if GPIO.input(mode) == GPIO.HIGH:
    #Set into batch mode
      #if (nextline == GPIO.HIGH and addline == GPIO.HIGH):
      #  nextline = GPIO.LOW
      #  addline = GPIO.LOW
      #Checks  for Invalid Case
            if incDgt == 1:
                incDgt = 0
                if n > 6:
                    n = 1
                    print(n)
                else:
                    n = n+1
                    print(n)
      #Moves the selected nth place number 
            if incLine == 1:
                incLine = 0
                batchsize = batchsize + 10**(n-1)
                if batchsize >= 9999999:
                  batchsize = 0
                print(batchsize)
      #Increments Batchsize Count by nth place number, Rolls over when overflow
        else:
      #Cont Mode
          batch=0
          batchsize = 0
          print("Hoopla")
          time.sleep(1)
      #Wipes informations
    ################
    #Post the Numbers onto the screen of the I2C LCD     **************************
    while GPIO.input(strtmenu) == GPIO.LOW:
        print("low")
        time.sleep(1)
