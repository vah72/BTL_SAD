from __future__ import unicode_literals
from django.shortcuts import render
from payment.models import payment_status as paystat
import requests
import json
def shipment_details_update(uname, orderid):
    ship_dict = {}
    ### It is used for getting data from payment info.
    payment = paystat.objects.filter(username=uname)
    for data in payment.values():
        data
    ship_dict['Order'] = data['order_id']
    ship_dict['Payment Status'] = data['status']
    
    url = 'http://127.0.0.1:8005/get_order_detail/{}'.format(orderid)
    response = requests.get(url).json()
    # print(response['data'][0]['product_id'])
    cart_id = response['data'][0]['cart_id']

    #get product info
    url1 = 'http://127.0.0.1:8006/get_cart/{}'.format(cart_id)
    response1 = requests.get(url1).json()
    ship_dict['Product Id'] = response1['data'][0]['product_id']
    ship_dict['Total'] = response['data'][0]['total']

    ### It is used for getting the user info.
    url = 'http://127.0.0.1:8000/userinfo/'
    d1 = {}
    d1["User Name"] = data['username']
    data = json.dumps(d1, default=str)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    ship_dict['First Name'] = val1['data']['First Name']
    ship_dict['Last Name'] = val1['data']['Last Name']
    ship_dict['Address'] = val1['data']['Address']
    ship_dict['Email Id'] = val1['data']['Email Id']
    ship_dict['Mobile Number'] = val1['data']['Mobile Number']
    ### Data is ready for calling the shipment_updates API.
    url = 'http://127.0.0.1:8002/shipment_updates/'
    data = json.dumps(ship_dict, default=str)
    print(data)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    api_resp = json.loads(response.content.decode('utf-8'))
    return api_resp
