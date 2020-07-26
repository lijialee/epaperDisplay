#!/usr/bin/python
# -*- coding:utf-8 -*-

from config import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback


epd = epd2in7.EPD()

'''2Gray(Black and white) display'''
epd.init()
epd.Clear(0xFF)


# Drawing on the Horizontal image
Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)
draw.line((20, 50, 70, 100), fill = 0)
draw.line((70, 50, 20, 100), fill = 0)
draw.rectangle((20, 50, 70, 100), outline = 0)
draw.line((165, 50, 165, 100), fill = 0)
draw.line((140, 75, 190, 75), fill = 0)
draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
draw.rectangle((80, 50, 130, 100), fill = 0)
draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
epd.display(epd.getbuffer(Himage))
time.sleep(2)

epd.sleep()


