import base64
import random
import string

with open("images/arewa.jpg", "rb") as image:
    data = image.read()

print(data)
print(type(data))

encodedImage = str(base64.b64encode(data))

print(encodedImage)
print(type(encodedImage))

# in a situation where provided data is originally not in base64
encodedImage = base64.b64encode(data).decode("utf-8")

decodedImage = base64.b64decode(encodedImage)

print(decodedImage)
print(type(decodedImage))

def generateFileName (strLength) : 
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k = strLength))
    return name;

fileName = generateFileName(7)

with open(f"data/{fileName}.png", "wb") as file:
    file.write(decodedImage)