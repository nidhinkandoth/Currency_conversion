from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
def conversion_page(request):
    return render(request, 'conversion_page.html')
@csrf_exempt
def conversion_api(request):
    #print request.POST
    amount = float(request.POST.get('amount'))
    convert_from = request.POST.get('convert_from')
    convert_to = request.POST.get('convert_to')
    if(convert_from == convert_to):
        return HttpResponse(amount)
    else:
        params = {'base':convert_from, 'symbols':convert_to}
        api = requests.get('http://api.fixer.io/latest', params=params)
        json_format = api.json()
        #print json_format
        #print convert_from
        #print convert_to
        #print amount
        #print converted_amount
        rate =float(json_format['rates'][convert_to])
        print rate
        converted_amount = amount * rate
        context = {'rate':rate}
        return HttpResponse(converted_amount)

