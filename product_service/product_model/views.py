from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from product_model.models import product_details

#lấy thông tin tất cả sản phẩm
@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    prodata = product_details.objects.all()
    for tbl_value in prodata.values():
        data.append(tbl_value)
    # If data is available then it returns the data.
        if data:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')
def getProdata(id):
    products = product_details.objects.filter(pk=id)
    for p in products.values():
        return p
    
def getProductByID(request, proid):
    resp = {}
    # This will fetch the data from the database.
    print(proid)
    data = getProdata(proid)
    if data:
        print(data)
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')

def getBookData(request):
    url='http://127.0.0.1:8008/get_all_books'
    headers= {'Content-Type' : 'application/json'}
    response = requests.get(url, headers=headers)
    book = json.loads(response.content.decode('utf-8'))
    return HttpResponse(json.dumps(book), content_type='application/json')

def getClotheData(request):
    url='http://127.0.0.1:8009/get_all_clothes'
    headers= {'Content-Type' : 'application/json'}
    response = requests.get(url, headers=headers)
    clothe = json.loads(response.content.decode('utf-8'))
    return HttpResponse(json.dumps(clothe), content_type='application/json')

def getShoeData(request):
    url='http://127.0.0.1:8008/get_all_shoes'
    headers= {'Content-Type' : 'application/json'}
    response = requests.get(url, headers=headers)
    shoe = json.loads(response.content.decode('utf-8'))
    return HttpResponse(json.dumps(shoe), content_type='application/json')