import sys
import logging
from sysFiles import epd2in13bc
import time
from PIL import Image, ImageDraw, ImageFont
import datetime
import dailyStuff

sys.path.insert(1, "./font")
sys.path.insert(1, "./pic")

logging.basicConfig(level=logging.DEBUG)

epdFile = epd2in13bc
epd = epd2in13bc.EPD()
epd.init()
print("Clear...")
epd.Clear()

# fonts
disneyFont = ImageFont.truetype('font/MouseMemoirs-Regular.ttf', 40)
luckiestGuyFont = ImageFont.truetype('font/LuckiestGuy-Regular.ttf', 15)
patrickHandFont = ImageFont.truetype('font/PatrickHand-Regular.ttf', 15)
righteousFont = ImageFont.truetype('font/Righteous-Regular.ttf', 15)


# Images
disneyImage = Image.open('pic/mouseLogo.png')
disneyImage = disneyImage.resize((40,40))


D2D = datetime.datetime(2021, 10, 19) - datetime.datetime.now()
D2DD = D2D.days
quote = str(dailyStuff.getQuote())
word = str(dailyStuff.getWord())

#29 characters in a line
def lineBreaker(string):
    output = string
    n = 0
    for i in output:
        n = n + 1
        if i == "\n":
            n = 0
        elif n % 29 == 0:
            x = output.rfind(" ", 0, n)
            output = output[:x]+'\n '+output[x+1:]
    return output


quote = lineBreaker(quote)
word = lineBreaker(word)


def printToDisplayDis(line1, line2, font1, font2, image):
    HBlackImage = Image.new('1', (epdFile.EPD_HEIGHT, epdFile.EPD_WIDTH), 255)
    HRedImage = Image.new('1', (epdFile.EPD_HEIGHT, epdFile.EPD_WIDTH), 255)

    drawb = ImageDraw.Draw(HBlackImage)
    drawr = ImageDraw.Draw(HRedImage)

    drawb.text((0, 0), line1, font=font1, fill=0)
    drawr.text((100, 50), line2, font=font2, fill=0)

    HBlackImage.paste(image, (150, 50))

    epd.display(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))

def printToDisplay(line1, line2, font1, font2):
    HBlackImage = Image.new('1', (epdFile.EPD_HEIGHT, epdFile.EPD_WIDTH), 255)
    HRedImage = Image.new('1', (epdFile.EPD_HEIGHT, epdFile.EPD_WIDTH), 255)

    drawb = ImageDraw.Draw(HBlackImage)
    drawr = ImageDraw.Draw(HRedImage)

    drawb.text((0, 0), line1, font=font1, fill=0)
    drawr.text((0, 15), line2, font=font2, fill=0)

    epd.display(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))


while True:
        printToDisplayDis("Days to Disney...", str(D2DD), disneyFont, disneyFont, disneyImage)

        time.sleep(30)

        printToDisplay("Quote of the Day...", quote, righteousFont, patrickHandFont)

        time.sleep(30)

        printToDisplay("Word of the Day...", word, luckiestGuyFont, patrickHandFont)

        time.sleep(30)
        
        epd.Clear()


