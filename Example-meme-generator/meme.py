from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO
print("gimme link")
url = input("link: ")
response = requests.get(url)
img = Image.open(BytesIO(response.content))
draw = ImageDraw.Draw(img)
print("gimme top text")
topText = input("top text: ").upper()
topFontSize = 1
img_fraction = 0.15
topFont = ImageFont.truetype("impact.ttf", topFontSize)
while topFont.getsize(topText)[1] < img_fraction*img.size[1]:
    topFontSize += 1
    topFont = ImageFont.truetype("impact.ttf", topFontSize)
draw.text((img.size[0]/2-topFont.getsize(topText)[0]/2,0),topText,(255,255,255),font=topFont)

print("gimme bottom text")
bottomText = input("bottom text: ").upper()
bottomFontSize = 1
img_fraction = 0.15
bottomFont = ImageFont.truetype("impact.ttf", bottomFontSize)
while bottomFont.getsize(bottomText)[1] < img_fraction*img.size[1]:
    bottomFontSize += 1
    bottomFont = ImageFont.truetype("impact.ttf", bottomFontSize)
draw.text((img.size[0]/2-bottomFont.getsize(bottomText)[0]/2,img.size[1]-bottomFont.getsize(bottomText)[1]),bottomText,(255,255,255),font=bottomFont)
img.save('sample-out.jpg')