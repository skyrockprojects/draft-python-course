from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO
fontFamily = "impact.ttf"
print("gimme file name")
name = input("name: ")
print("gimme link")
url = input("link: ")
response = requests.get(url)
img = Image.open(BytesIO(response.content))
draw = ImageDraw.Draw(img)
img_fraction = 0.15
desiredHeight = img_fraction*img.size[1]
desiredWidth = img.size[0]
def currentHeight(text, font):
    return font.getsize(text)[1]
def currentWidth(text, font):
    return font.getsize(text)[0]
def addText(text, yPos):
    fontSize = 1
    font = ImageFont.truetype(fontFamily, fontSize)
    while currentHeight(text, font) < desiredHeight and currentWidth(text, font) < desiredWidth:
        fontSize += 1
        font = ImageFont.truetype(fontFamily, fontSize)
    halfWidth = img.size[0]/2-font.getsize(text)[0]/2
    x = halfWidth
    y = yPos
    black = (0,0,0)
    white = (255,255,255)
    Left = (x-2, y-2)
    Right = (x+2, y-2)
    bottomRight = (x+2, y+2)
    bottomLeft = (x-2, y+2)
    draw.text(Left, text, black, font=font)
    draw.text(Right, text, black, font=font)
    draw.text(bottomRight, text, black, font=font)
    draw.text(bottomLeft, text, black, font=font)
    draw.text((x,y),text, white, font=font)
print("gimme top text")
topText = input("top text: ").upper()
topPos = 0
addText(topText, topPos)
print("gimme bottom text")
bottomText = input("bottom text: ").upper()
tempFontSize = 1
tempFont = ImageFont.truetype(fontFamily, tempFontSize)
while currentHeight(bottomText, tempFont) < desiredHeight and currentWidth(bottomText, tempFont) < desiredWidth:
        tempFontSize += 1
        tempFont = ImageFont.truetype(fontFamily, tempFontSize)
bottomPos = img.size[1]-tempFont.getsize(bottomText)[1]
addText(bottomText, bottomPos)
img.save(name+'.jpg')
img.show()