#from django.shortcuts import render
import os
from django.conf import settings
import requests
import datetime
from django.views.generic import FormView
from django.http import JsonResponse
from .forms import ZIPForms
logs_path = 'logs'

class Main(FormView):
    template_name = 'testwork/index.html'
    form_class = ZIPForms


def get_coords(request):
    zip_code = request.GET.get('zip_code', None)
    print('get_coords')
    text_request = 'https://www.zipcodeapi.com/rest/' + \
                   'I3otBhkSVpmCJrUZa5LcY8u8t3eZdjUKXLT7m2N80GaPXChB2kCVjkdlPryuFAYu/info.json/' + \
                   zip_code + '/degrees'

    resp = requests.get(text_request)
    msg = ''
    lat = ''
    lng = ''
    if resp.status_code != 200:
        msg_value = resp.json()['error_msg']
        msg = f'Error: {msg_value}'
    else:
        lat_value = resp.json()['lat']
        lng_value = resp.json()['lng']
        lat = f'Latitude: {lat_value}'
        lng = f'Longitude: {lng_value}'
    os.chdir(f'{settings.BASE_DIR}/{logs_path}')
    with open(f'{datetime.date.today()}.txt', 'a') as f:
        f.write(f'Request ZIP: {zip_code} - Answer: {msg} {lat} {lng}\n')

    data = {
        'lat': lat,
        'lng': lng,
        'msg': msg
    }
    return JsonResponse(data)

def get_intent(request):
    content = request.GET.get('content', None)

    key1 = 'd5667ab1088e4c108791a4e2eb0332cb'

    params = {
        # Query parameter
        'q': content,
        'subscription-key': key1,
    }

    resp  = requests.get(
            'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/3670e9d8-c8b0-4b4f-b8ab-c2188ae3238f',
            params=params)
    print(resp.json())
    if resp.status_code != 200:
        msg_value = resp.json()['error_msg']
        intent = f'Error: {msg_value}'
    else:
        intent = resp.json()['topScoringIntent']['intent']
    os.chdir(f'{settings.BASE_DIR}/{logs_path}')
    with open(f'{datetime.date.today()}.txt', 'a') as f:
        f.write(f'Request text: {content} - Answer: {intent}\n')
    data = {
        'intent': intent,
    }
    return JsonResponse(data)
