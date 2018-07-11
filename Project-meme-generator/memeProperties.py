from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO

def currentHeight(text, font):
    return font.getsize(text)[1]
def currentWidth(text, font):
    return font.getsize(text)[0]
fontFamily = "impact.ttf"
class 


class Meme:
    def __init__(self, imageURL, fileName, topText, bottomText):
        self.url = imageURL
        self.name = fileName
        self.top = topText
        self.bottom = bottomText
        self.getImage()
        self.addCaption()
    def requestFileName(self):
        print("gimme file name")
        self.name = input("name: ")
    def requestLink(self):
        print("gimme link")
        self.url = input("link: ")
    def getImage(self):
        response = requests.get(self.url)
        self.img = Image.open(BytesIO(response.content))
        self.draw = ImageDraw.Draw(self.img)
        self.img_fraction = 0.15
    def addCaption(self):
        topPos = 0
        self.addText(self.top.upper(), topPos)
        bottomText = self.bottom.upper()
        tempFontSize = 1
        tempFont = ImageFont.truetype(fontFamily, tempFontSize)
        while currentHeight(bottomText, tempFont) < self.desiredHeight and currentWidth(bottomText, tempFont) < self.desiredWidth:
                tempFontSize += 1
                tempFont = ImageFont.truetype(fontFamily, tempFontSize)
        bottomPos = self.img.size[1]-tempFont.getsize(bottomText)[1]
        self.addText(bottomText, bottomPos)
    def save(self):
        self.img.save(self.name+'.jpg')
    def show(self):
        self.img.show()
    def addText(self, text, yPos):
        self.desiredHeight = self.img_fraction*self.img.size[1]
        self.desiredWidth = self.img.size[0]
        fontSize = 1
        font = ImageFont.truetype(fontFamily, fontSize)
        while currentHeight(text, font) < self.desiredHeight and currentWidth(text, font) < self.desiredWidth:
            fontSize += 1
            font = ImageFont.truetype(fontFamily, fontSize)
        halfWidth = self.img.size[0]/2-font.getsize(text)[0]/2
        x = halfWidth
        y = yPos
        black = (0,0,0)
        white = (255,255,255)
        Left = (x-2, y-2)
        Right = (x+2, y-2)
        bottomRight = (x+2, y+2)
        bottomLeft = (x-2, y+2)
        self.draw.text(Left, text, black, font=font)
        self.draw.text(Right, text, black, font=font)
        self.draw.text(bottomRight, text, black, font=font)
        self.draw.text(bottomLeft, text, black, font=font)
        self.draw.text((x,y),text, white, font=font)