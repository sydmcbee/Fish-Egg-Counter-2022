from rpi_lcd import LCD
import math
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import cv2
#########################
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS,120)
global totcountstr
global totcount #Count Variable
global onBtcSkrn #On Batch Screen, Handles turn off
global BatchRstA #Batch reset for one button A & B
global BatchRstB
totcountstr = "0" #I made totcountstr because I needed to do string manipulation
totcount = 0
Numbatch = 0 #Batch number
onBtcSkrn = 0
BatchRstA = 0
BatchRstB = 0

########################
#VidCont Startup

lcd = LCD() #Calls LCD, there is a chance of LCD Errors that stops updating the lcd and it sucks

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
#SetupSwitch
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#Toggle Mode
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#Increment
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#Increment Line
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#Toggle Switch
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback2, bouncetime=30) # Setup event on pin 10 rising edge
GPIO.setup(22, GPIO.OUT) # Set pin 22 to be an output pin

#####################
#Starup Buttons Set
def fishImg(cam):
    ret, image = cam.read()
    cv2.imshow('Imagetest',image)
    im2 = cv2.resize(image,(150,150))
    im = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)
    t4 = time.time()
    cv2.imshow('Imagetest',im)

    cv2.imwrite('/media/pi/FilesOfFile/PtoSpm/{:f}+{:d}.jpg'.format(t4,lklcount),im,[int(cv2.IMWRITE_JPEG_QUALITY), 50])
    #Literally takes an image, sets it to RGB and compresses it to the next dimension
#############Take a Photo
def kmraAln(channel):
    global totcountstr
    global totcount
    totcount = totcount + 1
    #totcount = round(math.fmod(totcount,4))
    totcountstr = str(totcount)
    print(totcountstr)
    #Trigger interrupt. Named from older version, but it does also act as a camera trigger anyway
def incDgtFnc(channel):
    global incDgt
    global onBtcSkrn
    if onBtcSkrn == 1:
        global BatchRstA
        BatchRstA = 1
        onBtcSkrn = 0
    incDgt = 1
    #Green Button. These use a lot of global because interrupts are handled like a function
def incLnFnc(channel):
    global incLine
    global onBtcSkrn
    if onBtcSkrn == 1:
        global BatchRstB
        BatchRstB = 1
        onBtcSkrn = 0
    incLine = 1
    #Red button
    
GPIO.add_event_detect(10,GPIO.RISING,callback=kmraAln, bouncetime = 15) # Setup event on pin 10 rising edge
GPIO.add_event_detect(12,GPIO.RISING,callback=incDgtFnc, bouncetime =300) # Setup event on pin 10 rising edge
GPIO.add_event_detect(16,GPIO.RISING,callback=incLnFnc, bouncetime = 300) # Setup event on pin 10 rising edge
#Interrupt Setup, weirdly has to be below the functions, note the bouncetime.

###############
#some code to pull count & batch & batchsize
#Also does ErrorHandling if It remembers these things #Unused
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
mode=18
nextline=12
addline=16
try:
    n = 1


except:
    print("Button Setup Failed")
#Add Code to say button setup Failed *************

#############
global incDgt
global incLine
incDgt = 0
incLine = 0

while True:
    while GPIO.input(strtmenu) == GPIO.HIGH:
        #Set into Run or Setup
        GPIO.output(22,0) #motor off
        if GPIO.input(mode) == GPIO.HIGH:
        #Set into batch mode
        #Checks  for Invalid Case
            batchsize = str(batchsize).zfill(7)
            lcd.text((batchsize[:abs(7-n)]+'-'+batchsize[abs(7-n):]+" BchSize"),1)
            lcd.text(("Setup"),2)
            batchsize = int(batchsize)
            if incDgt == 1:
                incDgt = 0
                if n > 6:
                    #When selected nth place number exceeds, it loops back
                    batchsize = str(batchsize).zfill(7)
                    n = 1
                    lcd.clear()
                    lcd.text((batchsize[:abs(7-n)]+'-'+batchsize[abs(7-n):]+" BchSize"),1)
                    lcd.text(("Setup"),2)
                    batchsize = int(batchsize)

                else:
                    batchsize = str(batchsize).zfill(7)
                    n = n+1
                    lcd.clear()
                    lcd.text((batchsize[:abs(7-n)]+'-'+batchsize[abs(7-n):]+" BchSize"),1)
                    lcd.text(("Setup"),2)
                    batchsize = int(batchsize)
                    #Moves the selected nth place number 
            if incLine == 1:
                incLine = 0
                batchsize = batchsize + 10**(n-1)
                if batchsize >= 9999999:
                  batchsize = 0
                batchsize = str(batchsize).zfill(7)
                lcd.text((batchsize[:abs(7-n)]+'-'+batchsize[abs(7-n):]+" BchSize"),1)
                lcd.text(("Setup"),2)
                batchsize = int(batchsize)

                print(batchsize)
      #Increments Batchsize Count by nth place number, Rolls over when overflow
        else:
            n =1
            batchsize = 0
      #Cont Mode
        #Ignore the batchsize to set aspect
            batchsize = str(batchsize).zfill(7)
            lcd.text((batchsize[:abs(7-n)]+batchsize[abs(7-n):]+" ContMode"),1)
            lcd.text(("Setup"),2)
            batchsize = int(batchsize)
    ################
    while GPIO.input(strtmenu) == GPIO.LOW:
        #Running Mode 
        if totcount >= batchsize:
            #When in the batch wait mode ie the count exceeds the batchsize
            if batchsize != 0:
                GPIO.output(22,0)
                onBtcSkrn = 1
                #variable to handle moving to the next batch with buttons
                batchsize = str(batchsize).zfill(7)
                Numbatch = str(Numbatch)
                lcd.text(("Batch"+Numbatch+" "+totcountstr.zfill(7)),2)
                batchsize = int(batchsize)
                Numbatch = int(Numbatch)
                #numbatch refers to the batcher number
                if  BatchRstA == 1 and BatchRstB == 1:
                    #When in batch mode, if you push both buttons, it resets the count, inc batch number and keeps going 
                    BatchRstA = 0
                    BatchRstB = 0
                    totcount = 0
                    Numbatch = Numbatch +1
                    batchsize = str(batchsize).zfill(7)
                    Numbatch = str(Numbatch)
                    totcountstr=str(totcount)
                    lcd.text(("Batch"+Numbatch+" "+totcountstr.zfill(7)),2)
                    batchsize = int(batchsize)
                    Numbatch = int(Numbatch)
        if totcount < batchsize or batchsize == 0:
            #Running, just updating the count basically
            batchsize = str(batchsize).zfill(7)
            lcd.text((batchsize[:abs(7-n)]+batchsize[abs(7-n):]),1)
            lcd.text(("Running"+totcountstr.zfill(7)),2)
            batchsize = int(batchsize)
            GPIO.output(22,1)

            

