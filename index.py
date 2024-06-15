import base64
import random
import string
from urllib.request import urlopen
import requests


imageURI = input("Paste the link to the image: ")
imageExt = input("Input the desired file extension: ")
# print(type(imageURI))

# imageFile = urlopen(imageURI)

# encodedImage = base64.b64encode(urlopen(imageFile).read())

# decodedImage = base64.b64decode(encodedImage)

def generateFileName (strLength) : 
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k = strLength))
    return name;

fileName = generateFileName(7)

def encode_url_to_bytes(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    return base64.b64encode(requests.get(url, headers=headers, timeout=120).content).decode("utf-8")


def decode_to_image(f):
    return base64.b64decode(f)

convertedString = encode_url_to_bytes(imageURI)
decodedImage = decode_to_image(convertedString)

print(convertedString)
print(type(convertedString))

with open(f"data/{fileName}.{imageExt}", "wb") as f:
    f.write(decodedImage)

    print(":::::::::::::::::::::::::Download and conversion complete:::::::::::::::::::::::::")