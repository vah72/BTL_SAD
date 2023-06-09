from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Order
import requests

#lấy thông tin tất cả order
@csrf_exempt
def getAllOrder(request) :
    resp = {}
    data = []
    if request.method == 'GET':
        list_order = Order.objects.all()
        for order in list_order.values():
            data.append(order)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
    return HttpResponse(json.dumps(resp, default=str), content_type='application/json')

#Tạo một order mới với input là User Id và Cart Id
@csrf_exempt
def create_order(request):
    user_id = request.POST.get("User Id")
    cart_id = request.POST.get("Cart Id")
    print(cart_id)
    total =  getTotal(cart_id)
    print(total)
    shipment_id = request.POST.get("Shipment Id")
    resp = {}
    if user_id and cart_id and total and shipment_id:
        order = Order(user_id=user_id, cart_id=cart_id, total=total, shipment_id=shipment_id)
        if order:
            order.save()
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Create a new order successfully'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Data is invalid'
    else :
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory'
    return HttpResponse(json.dumps(resp, default=str), content_type='application/json')

#lấy tổng đơn hàng
def getTotal(card_id):
    #get list product through api cart
    url = 'http://127.0.0.1:8006/get_cart/{}'.format(card_id)
    listItem = requests.get(url).json()['data']
    product_id = listItem['product_id']
    quantity = listItem['quantity']
    url = 'http://127.0.0.1:8001/get_product_data/{}'.format(product_id)
    product= requests.get(url).json()['data']
    print(product)
    price = float(product['price'])
    return float(quantity)*price

#kiểm tra thông tin sản phẩm có tồn tại không
def checkProduct(id):
    url = 'http://127.0.0.1:8001/get_product_data/'
    listProduct = requests.get(url).json()
    for product in listProduct['data']:
        if product['product_id'] == id:
            return True
    return False

#xử lý nếu order thành công
def orderSuccess(request, order_id):
    resp = {}
    if request.method == 'DELETE':
        order = Order.objects.get(pk=order_id)
        print(order)
        order.delete()
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Update order successfully'
    else :
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Update order unsuccessfully'
    return HttpResponse(json.dumps(resp), content_type='application/json')

#lấy thông tin chi tiết một order theo id
def getOrderDetail(request, order_id):
    resp = {}
    data = []
    if request.method == 'GET':
        orders = Order.objects.filter(pk=order_id)
        for order in orders.values():
            order
        if order:
            data.append(order)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
        else :
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Error'
    return HttpResponse(json.dumps(resp, default=str), content_type='application/json')



