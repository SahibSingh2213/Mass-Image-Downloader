"""
Immage Downloader
 """

import requests
from io import BytesIO
from PIL import Image

search = input(">")
params = {'q': search}
r = requests.get("https://bing.com/images/search", params=params)
print("Status:", r.status_code)

image = Image.open(BytesIO(r.content))

path = "./image." + image.format

print(image.size, image.format)

try:
    image.save(path, image.format)
except IOError:
    print("cannot save image")
