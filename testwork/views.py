#from django.shortcuts import render
import requests
from django.views.generic import FormView, TemplateView
from django.http import JsonResponse
from .forms import ZIPForms


class Main(FormView):
    template_name = 'testwork/index.html'
    form_class = ZIPForms


def get_coords(request):
    zip_code = request.GET.get('zip_code', None)
    text_request = 'https://www.zipcodeapi.com/rest/' + \
                   '4mMHEGPGWlElFlDAYb1ttdPqAuL8f2Py13VVg7HUXvmPFXVWogwQubYz1D0wYqQn/info.json/' + \
                   zip_code + '/degrees'

    resp = requests.get(text_request)
    msg = ''
    lat = ''
    lng = ''
    if resp.status_code != 200:
        msg = resp.json()['error_msg']
    else:
        lat = resp.json()['lat']
        lng = resp.json()['lng']

    data = {
        'lat': lat,
        'lng': lng,
        'msg': msg
    }
    return JsonResponse(data)
