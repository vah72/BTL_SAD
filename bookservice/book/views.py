from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Book

# lấy thông tin tất cả sách
def getAllBooks(request):
    resp = {}
    data = []
    list_books = Book.objects.all()
    for book in list_books.values():
        data.append(book)
    resp['status'] = 'Success'
    resp['status_code'] = '200'
    resp['data'] = data
    return HttpResponse(json.dumps(resp), content_type='application/json')

#thêm sách mới
@csrf_exempt
def addBook(request):
    name = request.POST.get("Name")
    author = request.POST.get("Author")
    avai = request.POST.get("Available")
    price = request.POST.get("Price")
    resp = {}
    if name and author and avai and price:
        book = Book(name=name, author=author, availability=avai, price=price)
        if book:
            book.save()
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Add book successfully'
        else :
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = "Data is invalid"
    else :
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = "All fields are mandatory"
    return HttpResponse(json.dumps(resp), content_type='application/json')

 