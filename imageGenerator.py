#! /user/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageOps
 
def generateImage(size, date, hourMin, lineOne, lineTwo, symbolName = ""):
    img = Image.new('RGB', size, color = (255, 255, 255))
     
    dateImg = ImageDraw.Draw(img)
    dateFnt = ImageFont.truetype('Fonts/SpecialElite-Regular.ttf', 30)
    dateImg.text((0,0), date, font=dateFnt, fill=(0,0,0))
    
    
    hourMinImg = ImageDraw.Draw(img)
    hourMinFnt = ImageFont.truetype('Fonts/Carlito-Bold.ttf', 115)
    hourMinImg.text((0,22), hourMin, font=hourMinFnt, fill=(0,0,0))
    
    statusImg = ImageDraw.Draw(img)
    statusFnt = ImageFont.truetype('Fonts/Carlito-BoldItalic.ttf', 32)
    statusImg.text((0,115), lineOne, font=statusFnt, fill=(0,0,0))
    
    if symbolName == "downArrow":
        symbImg = Image.open('src/downArrow.png')
        img.paste(symbImg,(222,125))
    elif symbolName == "thinking":
        symbImg = Image.open('src/wave.png')
        symbImg = symbImg.resize((60,60))
        img.paste(symbImg,(215,115)) 
    
    statusImg2 = ImageDraw.Draw(img)
    statusImg2.text((0,146), lineTwo, font=statusFnt, fill=(0,0,0))
    
    
    img.save("testIMG.png")
    return img

test = generateImage((355,300), "1/23 Wednesday", "12", "323", "332", symbolName = "thinking")