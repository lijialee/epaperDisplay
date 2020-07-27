#!/usrbin/env python3
import os
os.chdir('/home/pi/Documents/epaperDisplay')

from config import epd2in7 
from PIL import Image, ImageDraw, ImageFont
import time
import imageGenerator
from gpiozero import LED


lineOne = "receiving parts"
lineTwo = " press the button"
print("loading")
#lut_partial_update
epd = epd2in7.EPD()
epd.init()
epd.Clear(0xFF)
print("cleaned")



def updateClock():
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
    img = imageGenerator.generateImage((epd.height, epd.width), date, hourMin, lineOne, lineTwo, symbolName = statusName)
    print("Got Img")
    epd.display(epd.getbuffer(img))
    print("updated")
    time.sleep(60)
    print("Next Cycle")
    updateClock()
    
updateClock()    