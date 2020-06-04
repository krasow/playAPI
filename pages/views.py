from django.shortcuts import render, redirect
import json
import requests
import random
from twilio.rest import Client
from .models import PhoneModel
from .forms import PhoneForm, VerifyForm
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


            response_image = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif')
            content = response_image.json()[0]
            image_url = content['url']

            response = requests.get('https://cat-fact.herokuapp.com/facts/random')
            content_text = response.json()
            cat_fact = content_text['text']


            client = Client(sid, token)


            if PhoneModel.objects.filter(to = form.cleaned_data['to']).exists():
                message = client.messages.create(
                    body= cat_fact,
                    from_='+12036338841',
                    media_url= image_url,
                    to= form.cleaned_data['to'],
                    )

                return redirect('home')
            else:
                service = client.verify.services.create(friendly_name='Cat verify')
                verification = client.verify \
                         .services(service.sid) \
                         .verifications \
                         .create(to=form.cleaned_data['to'], channel='sms')

                obj = form.save(commit=False)
                obj.sid = service.sid
                obj.save()
                form.save()
                return redirect ('verify')

    elif 'getcatsong' in request.POST:
        response = requests.get('https://api.deezer.com/search?q=track:"cat"')
        numResults = response.json()['total']

        payload = {'q': 'track:\"cat\"', 'index': random.randint(0, numResults-1)}
        response = requests.get('https://api.deezer.com/search', params=payload)
        content = response.json()['data'][random.randint(0,24)]
        songName = content['title']
        artist = content['artist']['name']
        albumURL = content['album']['cover_xl']
        return render(request,"index.html", {"songName": songName, "artist": artist, "albumURL": albumURL, "form": form})

    return render(request,"index.html", {"form":form})


def verify_cat(request):
    form = VerifyForm(request.POST)
    if form.is_valid():
        obj = PhoneModel.objects.order_by('-id')[0]
        client = Client(sid, token)
        verification_check = client.verify \
                .services(obj.sid) \
                .verification_checks \
                .create(to=obj.to, code=form.cleaned_data['code'])
        return redirect('home')

    return render(request,"verify.html", {"form":form})
