
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import user_registration


### This function is inserting the data into our table.
def data_insert(fname, lname, email, mobile, password, address):
    user_data = user_registration(fname=fname, lname=lname, email=email, mobile=mobile, password=password,
                                  address=address)
    user_data.save()
    return 1

@csrf_exempt
def registration_req(request):
    ### The Following are the input fields.
    fname = request.POST.get("First Name")
    lname = request.POST.get("Last Name")
    email = request.POST.get("Email Id")
    mobile = request.POST.get("Mobile Number")
    password = request.POST.get("Password")
    cnf_password = request.POST.get("Confirm Password")
    address = request.POST.get("Address")
    resp = {}
    #### In this if statement, checking that all fields are available.
    if fname and lname and email and mobile and password and cnf_password and address:
        if len(str(mobile)) == 10:
            if password == cnf_password:
                respdata = data_insert(fname, lname, email, mobile,
                                       password, address)
                ### If it returns value then will show success.
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['message'] = 'User is registered Successfully.'
                ### If it is not returning any value then the show will fail.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'Unable to register user, Please try again.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Password and Confirm Password should be same.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Mobile Number should be 10 digit.'

    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')

def getAllUser(request) :
    resp = {}
    data = []
    if request.method == 'GET':
        users = user_registration.objects.all()
        for user in users.values():
            data.append(user)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
    return HttpResponse(json.dumps(resp), content_type='application/json')