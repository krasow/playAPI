from django.shortcuts import render, redirect
import json
import requests
from twilio.rest import Client
from .models import PhoneModel
from .forms import PhoneForm
from .api import sid, token
# Create your views here.

def cat_view(request):
    form = PhoneForm()
    if 'getcat' in request.POST: 
        response = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif')
        content = response.json()[0]
        image_url = content['url']
        return render(request,"index.html", {"image_url": image_url, "form": form})

    elif 'getcatfact' in request.POST:
        response = requests.get('https://cat-fact.herokuapp.com/facts/random')
        content = response.json()
        cat_fact = content['text']
        return render(request,"index.html", {"cat_fact": cat_fact, "form": form})

    elif 'sendcat' in request.POST:
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            obj= PhoneModel.objects.order_by('-id')[0]

            response_image = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif')
            content = response_image.json()[0]
            image_url = content['url']

            response = requests.get('https://cat-fact.herokuapp.com/facts/random')
            content_text = response.json()
            cat_fact = content_text['text']

            account_sid = sid
            auth_token = token
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body= cat_fact,
                from_='+12036338841',
                media_url= image_url,
                to= obj.to,
            )

            return redirect('home')

    return render(request,"index.html", {"form":form})
