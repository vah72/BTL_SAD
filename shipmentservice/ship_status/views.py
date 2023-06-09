from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from ship_status.models import shipment as ship_obj


def ship_data_insert(fname, lname, email, mobile, address, shipment_status):
    shipment_data = ship_obj(fname=fname, lname=lname, email=email,
                             mobile=mobile,
                             address=address, 
                             shipment_status=shipment_status)
    shipment_data.save()
    return 1


#đăng ký một thông tin shipment mới
@csrf_exempt
def shipment_reg_update(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
    ### This is for reading the inputs from JSON.
            fname = val1.get("First Name")
            lname = val1.get("Last Name")
            email = val1.get("Email Id")
            mobile = val1.get("Mobile Number")
            address = val1.get("Address")
            shipment_status = "ready to dispatch"

            resp = {}

            respdata = ship_data_insert(fname, lname, email, mobile,
                                address, shipment_status)
            ### If it returns value then will show success.
            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Product is ready to dispatch.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Failed to update shipment details.'
    return HttpResponse(json.dumps(resp), content_type='application/json')
def shipment_data(uname):
     data = ship_obj.objects.filter(email = uname)
     for val in data.values():
        return val
### This function is used for getting the shipment status

#lấy thông tin trạng thái đơn hàng
@csrf_exempt
def shipment_status(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            variable1 = json.loads(request.body)
            ### This is for reading the inputs from JSON.
            uname = variable1.get("User Name")
            resp = {}
            ### It will call the shipment_data function.
            respdata = shipment_data(uname)
     ### If it returns value then will show success.
            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = respdata
     ### If it is not returning any value then it will showfailed response.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'User data is not available.'
    return HttpResponse(json.dumps(resp), content_type ='application/json')

#lấy thông tin tất cả shipment
def getAllShipment(request) :
    resp = {}
    data = []
    if request.method == 'GET':
        ship_objs = ship_obj.objects.all()
        for ship in ship_objs.values():
            data.append(ship)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
    return HttpResponse(json.dumps(resp), content_type='application/json')