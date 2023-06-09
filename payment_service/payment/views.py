from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from payment.models import payment_status as paystat
from shipment_update.views import shipment_details_update as ship_update
import requests

### This function is for fetching the user data.
def get_transaction_details(uname):
    payment = paystat.objects.filter(username=uname)
    for data in payment.values():
        return data


def store_data(uname, orderid):
    payment_data = paystat(username=uname, order_id=orderid, status="Success")
    payment_data.save()
    return 1

#lấy thông tin thanh toán
@csrf_exempt
def get_payment(request ):
    uname = request.POST.get("User Name")
    orderid = request.POST.get("Order id")
    resp = {}
    if uname and orderid :
        respdata = store_data(uname, orderid)
        respdata2 = ship_update(uname, orderid)
### If it returns value then will show success.
        if respdata:
            order_update(orderid=orderid)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Transaction is completed.'
### If it is returning null value then it will show failed.
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Transaction is failed, Please try again.'
            ### If any mandatory field is missing then it will be through a
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')
### This function is created for getting the username and password.

#cập nhật danh sách order sau khi thanh toán thành công
def order_update(orderid):
    url = "http://127.0.0.1:8005/update_order/{}".format(orderid)
    response = requests.delete(url)

#lấy thông tin giao dịch
@csrf_exempt
def user_transaction_info(request):
    # uname = request.POST.get("User Name")
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            uname = val1.get('User Name')
            resp = {}
        if uname:
            ## Calling the getting the user info.
            respdata = get_transaction_details(uname)
            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['data'] = respdata
    ### If a user is not found then it give failed as response.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'User Not Found.'
        else:
             resp['status'] = 'Failed'
             resp['status_code'] = '400'
             resp['message'] = 'Fields is mandatory.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'
    return HttpResponse(json.dumps(resp), content_type='application/json')


def getAllPayment(request) :
    resp = {}
    data = []
    if request.method == 'GET':
        list_pay = paystat.objects.all()
        for pay in list_pay.values():
            data.append(pay)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
    return HttpResponse(json.dumps(resp), content_type='application/json')
