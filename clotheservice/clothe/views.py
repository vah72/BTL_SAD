from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Clothe


def getAllClothes(request):
    resp = {}
    data = []
    list_clothes = Clothe.objects.all()
    for clothe in list_clothes.values():
        data.append(clothe)
    resp['status'] = 'Success'
    resp['status_code'] = '200'
    resp['data'] = data
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def addClothe(request):
    name = request.POST.get("Name")
    brand = request.POST.get("brand")
    avai = request.POST.get("Available")
    price = request.POST.get("Price")
    resp = {}
    if name and brand and avai and price:
        clothe = Clothe(name=name, brand=brand, availability=avai, price=price)
        if clothe:
            clothe.save()
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Add clothe successfully'
        else :
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = "Data is invalid"
    else :
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = "All fields are mandatory"
    return HttpResponse(json.dumps(resp), content_type='application/json')

 