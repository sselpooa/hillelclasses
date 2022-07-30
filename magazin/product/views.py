from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product


def index(request):
    return render(request,'base.html')


def get_all_products(request):
    context = {
        'products' : Product.objects.order_by('status', 'id'),
        'title' : 'All products'
    }
    return render(request, 'all.html', context)

def get_by_status(request,status):
    products = Product.objects.filter(status=status)
    response = f'<h1>За статусом {status} знайдено такі товари:<h1>'
    for product in products:
        response += f'{product.title}-{product.performer}<br>'
    return HttpResponse(response)

def get_detail(request,prd_id):
    try:
        product = Product.objects.get(id=prd_id)
    except Product.DoesNotExist:
        return HttpResponse('Такого товару немає')
    return HttpResponse(product.description)

def get_by_performer(request,performer):
    products = Product.objects.filter(performer=performer)
    response = f'<h1>Магазин має такі товари від виконавця {performer}<h1>'
    for product in products:
        response += f'{product.title}<br>'
    return render(response)

def get_by_genre(request,genre):
    products = Product.objects.filter(genre=genre)
    response = f'<h1>Магазин має такі товари за жанром {genre}<h1>'
    for product in products:
        response += f'{product.title}<br>'
    return render(response)


