#!/usrbin/env python3
import os
os.chdir('/home/pi/Documents/epaperDisplay')
from config import epd2in7
from gpiozero import PWMLED, Button
import RPi.GPIO as GPIO 
import imageGenerator
import time
import threading

#Global Var
greenMessage1 = ""
greenMessage2 = ""
yellowMessage1 = "receiving parts"
yellowMessage2 = " press the button"
redMessage1 = "will back soon"
redMessage2 = ""

lineOne = ""
lineTwo = ""

#Epaper set up
print("loading")
#lut_partial_update
epd = epd2in7.EPD()
epd.init()
epd.Clear(0xFF)
print("cleaned")

#GPIO setup
greenLed = PWMLED("BOARD33")
yellowLed = PWMLED("BOARD35")
redLed = PWMLED("BOARD37")

greenButton = Button("BOARD36")
yellowButton = Button("BOARD38")
redButton = Button("BOARD40", hold_time=5)


greenLed.on()
#Epaper function
def updateEpaperLoop():
    month = time.strftime("%m")
    day = time.strftime("%d")
    wk_day = time.strftime("%A")
    hour_number = time.strftime("%H")
    min_number = time.strftime("%M")
    sec_number = time.strftime("%S")
    date = month + "/" + day + " " + wk_day
    hourMin = hour_number + ":" + min_number
    print("Got time")
    statusName = "thinking"
    img = imageGenerator.generateImage((epd.height, epd.width), date, hourMin, lineOne, lineTwo, greenMessage1, yellowMessage1, redMessage1)
    print("Got Img")
    epd.display(epd.getbuffer(img))
    print("updated")
    t = threading.Timer(60,updateEpaperLoop)
    t.start()
    print("Next Cycle")
updateEpaperLoop()    


def updateEpaper():
    month = time.strftime("%m")
    day = time.strftime("%d")
    wk_day = time.strftime("%A")
    hour_number = time.strftime("%H")
    min_number = time.strftime("%M")
    sec_number = time.strftime("%S")
    date = month + "/" + day + " " + wk_day
    hourMin = hour_number + ":" + min_number
    print("Got time")
    statusName = "thinking"
    img = imageGenerator.generateImage((epd.height, epd.width), date, hourMin, lineOne, lineTwo, greenMessage1, yellowMessage1, redMessage1)
    print("Got Img")
    epd.display(epd.getbuffer(img))
    print("Finish update")  




def greenLedPressed():
    global lineOne
    global lineTwo
    if lineOne != greenMessage1:
        yellowLed.off()
        redLed.off()
        greenLed.on()
        lineOne = greenMessage1
        lineTwo = greenMessage2
        updateEpaper()
    
def yellowLedPressed():
    global lineOne
    global lineTwo
    if lineOne != yellowMessage1:
        greenLed.off()
        redLed.off()
        yellowLed.pulse()
        lineOne = yellowMessage1
        lineTwo = yellowMessage2
        updateEpaper()

def redLedPressed():
    global lineOne
    global lineTwo
    if lineOne != redMessage1:
        yellowLed.off()
        greenLed.off()
        redLed.pulse()
        lineOne = redMessage1
        lineTwo = redMessage2
        updateEpaper()

def allLedOn():
    greenLed.on()
    redLed.on()
    yellowLed.on()
    
def allLedOff():
    greenLed.off()
    redLed.off()
    yellowLed.off()
    
def shutAllDown():
    allLedOn()
    epd.Clear(0xFF)
    epd.sleep()
    time.sleep(1)
    allLedOff()
    GPIO.cleanup()
    os.system("shutdown now -h")
      
greenButton.when_pressed = greenLedPressed
yellowButton.when_pressed = yellowLedPressed
redButton.when_pressed = redLedPressed

redButton.when_held = shutAllDown






