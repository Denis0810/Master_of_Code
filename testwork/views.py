#from django.shortcuts import render
import requests
import json
import http.client, urllib.request, urllib.parse, urllib.error, base64
from django.views.generic import FormView, TemplateView
from django.http import JsonResponse
from .forms import ZIPForms, AIForm


class Main(FormView):
    template_name = 'testwork/index.html'
    form_class = ZIPForms


def get_coords(request):
    zip_code = request.GET.get('zip_code', None)
    print('get_coords')
    key1 = '5a1429b4a2934f05997b785d96e6dc43'
    key2 = 'c2143459c1e946b488effa3237925526'
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

    data = {
        'lat': lat,
        'lng': lng,
        'msg': msg
    }
    return JsonResponse(data)

class AIView(FormView):
    template_name = 'testwork/ai.html'
    form_class = AIForm


def get_intent(request):
    content = request.GET.get('content', None)
    key1 = '5a1429b4a2934f05997b785d96e6dc43'
    key2 = 'c2143459c1e946b488effa3237925526'
    #understanding
    key3 = 'fdbfc549a6294bfe9fb3e6d537e76cee'
    key4 = 'd239aa80db484e3aac48f07dee8db449'

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': key3,
    }

    params = {
        # Query parameter
        'q': content,
        # Optional request parameters, set to default values
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }

    try:
        r = requests.get(
            'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/3670e9d8-c8b0-4b4f-b8ab-c2188ae3238f ',
            headers=headers, params=params)
        print(r.json())

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


    print(r)
    data = {
        'intent':'',
    }
    return JsonResponse(data)
