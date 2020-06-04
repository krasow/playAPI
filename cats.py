import json
import requests

response = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif')
content = response.json()[0]
image_url = content['url']
print(image_url)

response = requests.get('https://cat-fact.herokuapp.com/facts/random')
content = response.json()
print(content['text'])

from twilio.rest import Client
account_sid = 'AC25ca77208be7bb8ceaf5519050be11e5'
auth_token = 'd8c96c959f8c9c7086b60c2b999b1d0e'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=content['text'],
    media_url=image_url,
    from_='+16122556455',
    to='+18287133117',
)
print(message.sid)
