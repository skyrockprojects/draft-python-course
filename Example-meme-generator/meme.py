from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO
url = "https://i.ytimg.com/vi/lEPc9xi0Tt0/hqdefault.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("sans-serif.ttf", 16)