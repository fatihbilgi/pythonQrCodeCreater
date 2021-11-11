import requests
from PIL import Image
from io import BytesIO

url = "https://" + input("Enter the URL: ")

endpoint = "https://api.qrserver.com/v1/create-qr-code/"

orn = f"?data={url}&amp:size=500x500"
color = "&color=113C4F"
response = requests.get(endpoint + orn + color)

img = Image.open(BytesIO(response.content))

img.save("qr.png")
