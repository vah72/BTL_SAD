from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from .models import product_comment
from django.http import HttpResponse
# Create your views here.
@csrf_exempt
def add_comment(request):
    uname = request.POST.get("User Name")
    proid = request.POST.get("Product id")
    comment = request.POST.get("Comment")
    rating = request.POST.get("Rating") # one to five star
    # user_id = models.IntegerField()
    # product_id = models.IntegerField()

    url = "http://127.0.0.1:8001/get_product_data/{}".format(proid)
    d1 = {}
    # d1["User Name"] = uname
    # d1['Product Id'] = proid
    # data = json.dumps(d1)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    product_name = val1.get("data").get("product_name")
    respdata =comment_data_insert(comment=comment, product_id= proid, rating=rating, uname=uname)
    resp = {}
    if respdata:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Product is ready to dispatch.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Failed to update shipment details.'
    return HttpResponse(json.dumps(resp), content_type='application/json')

    # if var1
    #
@csrf_exempt
def show_product_comment(request):
    uname = request.POST.get("User Name")
    proid = request.POST.get("Product id")
    comments = product_comment.objects.filter(product_id=proid, uname=uname)

    data = []
    resp = {}
    # This will fetch the data from the database.
    for tbl_value in comments.values():
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
def getProComment(product_id, uname):
    comments = product_comment.objects.filter(product_id=product_id, uname=uname)
    return comments
def comment_data_insert(comment,product_name, proid, rating, uname) :
    comment = product_comment(comment=comment, product_name=product_name, product_id=proid,
                     rating=rating, uname=uname
                     )
    comment.save()
    return 1
# def getProductByID(request):