from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO
url = "https://i.ytimg.com/vi/lEPc9xi0Tt0/hqdefault.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
draw = ImageDraw.Draw(img)
topText = "Obunga"
topFontSize = 1
img_fraction = 0.15
topFont = ImageFont.truetype("impact.ttf", topFontSize)
while topFont.getsize(topText)[1] < img_fraction*img.size[1]:
    topFontSize += 1
    topFont = ImageFont.truetype("impact.ttf", topFontSize)
draw.text((img.size[0]/2-topFont.getsize(topText)[0]/2,0),topText,(255,255,255),font=topFont)
img.save('sample-out.jpg')