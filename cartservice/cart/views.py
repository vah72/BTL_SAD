from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Cart

#lấy thông tin tất cả giỏ hàng
def getAllCartItem(request):
    resp = {}
    data = []
    list_cart_items = Cart.objects.all()
    for cart_item in list_cart_items.values():
        data.append(cart_item)
    resp['status'] = 'Success'
    resp['status_code'] = '200'
    resp['data'] = data
    return HttpResponse(json.dumps(resp), content_type='application/json')


#lấy thông tin các sản phẩm trong giỏ hàng theo người dùng
def getCartItemByUser(request,user_id):
    resp = {}
    data = []
    list_cart_items = Cart.objects.filter(user_id=user_id)
    if len(list_cart_items) == 0 :
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = f"User {user_id} haven't add any product yet"
    else :
        for cart_item in list_cart_items.values():
            data.append(cart_item)
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    return HttpResponse(json.dumps(resp), content_type='application/json')

#lấy thông tin sản phẩn trong giỏ hàng theo id
def getCartItemById(request,cart_id):
    resp = {}
    cart = Cart.objects.filter(pk=cart_id).values()[0]
    print(cart)
    if cart :
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = cart
        print(cart)
    else :
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Not found cart'
    return HttpResponse(json.dumps(resp), content_type='application/json')

#thêm sản phẩm vào giỏ hàng
@csrf_exempt
def add_to_cart(request):
    user_id = request.POST.get("User Id")
    product_id = request.POST.get("Product Id")
    quantity = request.POST.get("Quantity")
    resp = {}
    if user_id and product_id and quantity:
        cart = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
        cart.save()
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Add to cart successfully'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = "All fields are mandatory"
    return HttpResponse(json.dumps(resp), content_type='application/json')
#cập nhật giỏ hàng
@csrf_exempt
def update_cart(request, cart_id):
    if request.method == 'POST':
        quantity = request.POST.get("Quantity")
        resp = {}
        list_cart = Cart.objects.filter(pk=cart_id).values()
        if len(list_cart) > 0:
            cart = list_cart[0]
            cart_update = Cart(pk=cart_id, user_id=cart['user_id'], product_id=cart['product_id'],
                            quantity=quantity)
            cart = Cart.objects.get(pk=cart_id)
            cart.delete()
            cart_update.save()
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Update to cart successfully'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = f"Not found cart {cart_id}"
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = "Failed"
    return HttpResponse(json.dumps(resp), content_type='application/json')

#xóa giỏ hàng
@csrf_exempt
def delete_cart(request, cart_id):
    resp = {}
    if request.method == 'DELETE':
        cart = Cart.objects.get(pk=cart_id)
        if cart:
            print(cart)
            cart.delete()
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Delete cart successfully'
        else :
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = f"Not found {cart_id}"
    else :
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Delete cart unsuccessfully'
    return HttpResponse(json.dumps(resp), content_type='application/json')

        

    
    
