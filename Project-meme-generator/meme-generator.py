from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO

# class Meme:
#     def __init__(self, picture, topText, bottomText):
#         self.picture = picture
#         self.topText = topText
#         self.bottomText = bottomText

#     def print(self):
#         print(self.topText)
#         print(self.picture)
#         print(self.bottomText)

#     def toString(self):
#         return self.topText + "\n" + self.picture + "\n" + self.bottomText

message = ""
print("gimme link")
message = input("link: ")
response = requests.get(message.strip())
img = Image.open(BytesIO(response.content))
print("gimme top text")
message = input("top text: ")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("impact.ttf", 50)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),message.upper(),(0,0,0),font=font)
print("gimme bottom text")
message = input("bottom text: ")
img.save('sample-out.jpg')
