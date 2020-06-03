import json
import requests

response = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif')
content = response.json()[0]
image_url = content['url']
print(image_url)
