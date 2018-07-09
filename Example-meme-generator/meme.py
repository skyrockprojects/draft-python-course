from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO
url = "https://i.ytimg.com/vi/lEPc9xi0Tt0/hqdefault.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
draw = ImageDraw.Draw(img)
txt = "Obunga"
fontsize = 1
img_fraction = 0.15
font = ImageFont.truetype("impact.ttf", fontsize)
while font.getsize(txt)[1] < img_fraction*img.size[1]:
    fontsize += 1
    font = ImageFont.truetype("impact.ttf", fontsize)
draw.text((img.size[0]/2-font.getsize(txt)[0]/2,0),txt,(255,255,255),font=font)
img.save('sample-out.jpg')