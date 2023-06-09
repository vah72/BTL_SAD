from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Shoe

# Create your views here.
def getAllShoes(request):
    resp = {}
    data = []
    list_shoes = Shoe.objects.all()
    for shoe in list_shoes.values():
        data.append(shoe)
    resp['status'] = 'Success'
    resp['status_code'] = '200'
    resp['data'] = data
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def addShoe(request):
    name = request.POST.get("Name")
    brand = request.POST.get("Brand")
    avai = request.POST.get("Available")
    price = request.POST.get("Price")
    resp = {}
    if name and brand and avai and price:
        shoe = Shoe(name=name, brand=brand, availability=avai, price=price)
        if shoe:
            shoe.save()
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Add shoe successfully'
        else :
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = "Data is invalid"
    else :
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = "All fields are mandatory"
    return HttpResponse(json.dumps(resp), content_type='application/json')

 