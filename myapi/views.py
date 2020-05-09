from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib.parse
import json
# Create your views here.

def translate(diabetes):
    diabetes_encoded = urllib.parse.quote(diabetes.text[:236])
    diabetes_ar = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20200508T202221Z.8110a46d13d7c2f7.da36b5b0950f125ff1d16682c15cba3aae6c7f66&text="+diabetes_encoded+"&lang=ar&format=plain")
    return diabetes_ar


def top_items_to_consume(request):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/topitemstoconsume?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16')
    return HttpResponse(translate(diabetes), content_type='text/json')

def suggest(request, fg2):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/suggest?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16&fg2='+fg2+'')
    return HttpResponse(translate(diabetes), content_type='text/json')

def top_items_to_avoid(request):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/topitemstoavoid?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16')
    return HttpResponse(translate(diabetes), content_type='text/json')

def detailed_helpful_list(request, fg1):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/detailedhelpfullist?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16&fg1='+fg1+'')
    return HttpResponse(translate(diabetes), content_type='text/json')

def detailed_harmful_list(request, fg1):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/detailedHarmfulList?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16&fg1=' + fg1 + '')
    return HttpResponse(translate(diabetes), content_type='text/json')

def detailed_neutral_list(request, fg1):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/detailedNeutralList?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16&fg1=' + fg1 + '')
    return HttpResponse(translate(diabetes), content_type='text/json')

def good_for(request, b):
    diabetes = requests.get("https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/goodfor?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&itemID="+str(b)+"&problemId=16")
    return HttpResponse(translate(diabetes), content_type='text/json')

def food_groups(request):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/foodgroups?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c')
    return HttpResponse(translate(diabetes), content_type='text/json')

def health_conditions(request):
    diabetes = requests.get("https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/healthconditions?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c")
    return HttpResponse(translate(diabetes), content_type='text/json')

def food_items(request, fg, condition, value):
    diabetes = requests.get("https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/fooditems?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&fg="+fg+"&condition="+condition+"&value="+value)
    return HttpResponse(translate(diabetes), content_type='text/json')

