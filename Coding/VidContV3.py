import cv2
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import picamera

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#########################
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS,120)
totcount = 0;
picamera.shutter_speed = 2000
########################
def fishImg(cam):
    global totcount
    t1=time.time()
    ret, image = cam.read()
    #cv2.imshow('Imagetest',image)
    im2 = cv2.resize(image,(150,150))
    im = cv2.cvtColor(im2, cv2.COLOR_BGR2HSV)
    im = cv2.blur(im, (5,5))
    #msk = cv2.inRange(im, (0,70,100),(100,255,255))
    msk = cv2.inRange(im, (0,150,100),(360,255,255))
    msk = cv2.blur(msk, (7,7))
    contours, hierarchy = cv2.findContours(msk, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    lklcount = 0
    for n in range(0,len(contours)):
        arc = cv2.arcLength(contours[n],1)
        #print(arc)
        if arc >= 35:
        #Distant Eggs ~40, Close ~120
            lklcount= lklcount+1
    print(lklcount)
    totcount = totcount + lklcount
    #cv2.imshow('Imagetest',msk)
    cv2.imshow('Imagetest',im2)
    t4=time.time()

    cv2.imwrite('/home/pi/FtoSpm/{:f}.jpg'.format(t4),im2,[int(cv2.IMWRITE_JPEG_QUALITY), 50])
    t4=time.time()
    print(t4-t1)
    k = cv2.waitKey(1)
    #if k != -1:
        #break
    return lklcount

def kmraAln(channel):
    if GPIO.input(10):
        fishImg(cam)

GPIO.add_event_detect(10,GPIO.RISING,callback=kmraAln, bouncetime = 30) # Setup event on pin 10 rising edge

#######################
#cam.release()
#cv2.destroyAllWindows()



