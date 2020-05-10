from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib.parse
import json
# Create your views here.
'''''
def translate(diabetes):
    diabetes_encoded = urllib.parse.quote(diabetes.text[:9000])
    diabetes_ar = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20200508T202221Z.8110a46d13d7c2f7.da36b5b0950f125ff1d16682c15cba3aae6c7f66&text="+diabetes_encoded+"&lang=ar&format=plain")
    return diabetes_ar
'''''

def top_items_to_consume(request):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/topitemstoconsume?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16')
    return HttpResponse(diabetes.text, content_type='text/json')

def suggest(request, fg2):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/suggest?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16&fg2='+fg2+'')
    return HttpResponse(diabetes.text, content_type='text/json')

def top_items_to_avoid(request):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/topitemstoavoid?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16')
    return HttpResponse(diabetes.text, content_type='text/json')

def detailed_helpful_list(request, fg1):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/detailedhelpfullist?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16&fg1='+fg1+'')
    return HttpResponse(diabetes.text, content_type='text/json')

def detailed_harmful_list(request, fg1):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/detailedHarmfulList?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16&fg1=' + fg1 + '')
    return HttpResponse(diabetes.text, content_type='text/json')

def detailed_neutral_list(request, fg1):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/detailedNeutralList?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&problemId=16&fg1=' + fg1 + '')
    return HttpResponse(diabetes.text, content_type='text/json')

def good_for(request, b):
    diabetes = requests.get("https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/goodfor?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&itemID="+str(b)+"&problemId=16")
    return HttpResponse(diabetes.text, content_type='text/json')

def food_groups(request):
    diabetes = requests.get('https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/foodgroups?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c')
    return HttpResponse(diabetes.text, content_type='text/json')

def health_conditions(request):
    diabetes = requests.get("https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/healthconditions?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c")
    return HttpResponse(diabetes.text, content_type='text/json')

def food_items(request, fg, condition, value):
    diabetes = requests.get("https://nutridigm-api-dev.azurewebsites.net/api/v1/nutridigm/fooditems?subscriptionId=8d0f640d-c991-1320-4977-1b0fec7f610c&fg="+fg+"&condition="+condition+"&value="+value)
    return HttpResponse(diabetes.text, content_type='text/json')

def init_session(request):
    sessionid = json.loads(requests.get("http://api.endlessmedical.com/v1/dx/InitSession").text)
    session = sessionid['SessionID']
    return HttpResponse(session, content_type='text/json')

def accept_terms_of_use(request):
    try:
        sessionid = request.POST['sessionId']
        accept = requests.post("http://api.endlessmedical.com/v1/dx/AcceptTermsOfUse?SessionID="+sessionid+"&passphrase=I%20have%20read%2C%20understood%20and%20I%20accept%20and%20agree%20to%20comply%20with%20the%20Terms%20of%20Use%20of%20EndlessMedicalAPI%20and%20Endless%20Medical%20services.%20The%20Terms%20of%20Use%20are%20available%20on%20endlessmedical.com")
        if accept.status_code == 200:

            return HttpResponse('you have accepted the terms', content_type='text/json')
        else:
            return HttpResponse("failed", content_type='text/json')
    except:
        return HttpResponse("failed", content_type='text/json')

def get_use_default_values(request, sessionid):
    value = requests.get("http://api.endlessmedical.com/v1/dx/GetUseDefaultValues?SessionID="+sessionid+"")
    return HttpResponse(value.text, content_type='text/json')

def get_out_comes(request):
    outcomes = requests.get("http://api.endlessmedical.com/v1/dx/GetOutcomes")
    return HttpResponse(outcomes.text, content_type='text/json')

def get_features(request):
    features = requests.get("http://api.endlessmedical.com/v1/dx/GetFeatures")
    return HttpResponse(features.text, content_type='text/json')

def set_use_default_values(request, sessionId, boolean):
    set = requests.post("http://api.endlessmedical.com/v1/dx/SetUseDefaultValues?SessionID="+sessionId+"&value="+boolean)
    return HttpResponse(set.text, content_type='text/json')

def update_feature(request, sessionId, feature, boolean):
    update = requests.post("http://api.endlessmedical.com/v1/dx/UpdateFeature?SessionID="+sessionId+"&name="+feature+"&value="+boolean)
    return HttpResponse(update.text, content_type='text/json')
def delete_feature(request, sessionId,feature):
    delete = requests.post("http://api.endlessmedical.com/v1/dx/DeleteFeature?SessionID="+sessionId+"&name="+feature+"")
    return HttpResponse(delete.text, content_type='text/json')





