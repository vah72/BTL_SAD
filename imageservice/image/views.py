from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Image

@csrf_exempt
def add_image(request, product_id):
    prod_id = product_id
    url = request.POST.get('URL')
    des = request.POST.get('Description')
    resp = {}
    if url and des:
        image = Image(product_id=prod_id, url=url, description=des)
        if image:
            image.save()
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = f"Add image to product {prod_id} successfully"
        else :
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = f"Data is invalid"
    else: 
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = f"All fields are mandatory"
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def delete_image(request, product_id):
    resp= {}
    if request.method == 'DELETE':
        images = Image.objects.filter(product_id=product_id)
        for image in images:
            image.delete()
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = f"Delete image successfully"
    else :
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = f"Failed method"
    return HttpResponse(json.dumps(resp), content_type='application/json')

def getAllImage(request):
    resp={}
    data=[]
    images = Image.objects.all()
    for image in images.values():
        data.append(image)
    resp['status'] = 'Success'
    resp['status_code'] = '200'
    resp['data'] = data
    return HttpResponse(json.dumps(resp), content_type='application/json')