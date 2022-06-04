import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BOARD)
SmplPnt = []
i = (0)
count12 = 0 # this is the middle sensor
count10 = 0 # this is the fourth sensor
count8 = 0 # this is the first sensor
count16 = 0 # this is the fifth sensor
count18 = 0 # this is the second sensor
GPIO.setup(12, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(16, GPIO.IN)
while (1==1):
    for i in range(1,100):
        if GPIO.input(12):
            #print("pin 12 is high")
            a=1

        else:
            print("pin 12:")
            a=0
            count12 = count12 + 1
            print(count12)
        time.sleep(.015)
        SmplPnt.append(a)

        if GPIO.input(10):
            #print("pin 12 is high")
            a=1

        else:
            print("pin 10:")
            a=0
            count10 = count10 + 1

            print(count10)
        time.sleep(.015)
        SmplPnt.append(a)

        if GPIO.input(8):
            #print("pin 12 is high")
            a=1

        else:
            print("pin 8:")
            a=0
            count8 = count8 + 1

            print(count8)
        time.sleep(.015)
        SmplPnt.append(a)

        if GPIO.input(18):
            #print("pin 12 is high")
            a=1

        else:
            print("pin 18:")
            a=0
            count18 = count18 + 1

            print(count18)
        time.sleep(.015)
        SmplPnt.append(a)

        if GPIO.input(16):
            #print("pin 12 is high")
            a=1

        else:
            print("pin 16:")
            a=0
            count16 = count16 + 1

            print(count16)
        time.sleep(.015)
        SmplPnt.append(a)
        print("total=")
        print(count16+count18+count10+count8+count12)

