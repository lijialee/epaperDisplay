#! /user/bin/env python3
from PIL import Image, ImageDraw, ImageFont
 
def generateImage(size, date, hourMin, lineOne, lineTwo):
    img = Image.new('RGB', size, color = (255, 255, 255))
     
    dateImg = ImageDraw.Draw(img)
    dateFnt = ImageFont.truetype('Fonts/Carlito-Bold.ttf', 30)
    dateImg.text((0,0), date, font=dateFnt, fill=(0,0,0))
    
    
    hourMinImg = ImageDraw.Draw(img)
    hourMinFnt = ImageFont.truetype('Fonts/Carlito-Bold.ttf', 115)
    hourMinImg.text((0,22), hourMin, font=hourMinFnt, fill=(0,0,0))
    
    statusImg = ImageDraw.Draw(img)
    statusFnt = ImageFont.truetype('Fonts/Carlito-BoldItalic.ttf', 32)
    statusImg.text((0,120), lineOne, font=statusFnt, fill=(0,0,0))
    
    statusImg2 = ImageDraw.Draw(img)
    statusImg2.text((0,150), lineTwo, font=statusFnt, fill=(0,0,0))
    img.save("testIMG.png")
    return img

#generateImage((255,255), "123", "12", "323", "332")