from config import epd2in7
from PIL import Image, ImageDraw, ImageFont
import imageGenerator
import time

lineOne = ""
lineTwo = ""
print("loading")
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
    date = month + "/" + day 
    hourMin = hour_number + ":" + min_number
    print("Got time")
    img = imageGenerator.generateImage((epd.height, epd.width), date, hourMin, lineOne, lineTwo)
    print("Got Img")
    epd.display(epd.getbuffer(img))
    print("updated")
    time.sleep(10)
    print("Next Cycle")
    updateClock()
    
updateClock()    