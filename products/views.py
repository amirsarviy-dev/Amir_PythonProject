from django.http import JsonResponse
from products.models import Product
from products.forms import ProductFrom


def get_products(request):
    if request.method == 'GET':
        return JsonResponse(list(Product.objects.all().values('name','price')), safe=False)
    elif request.method == 'POST':
        form = ProductFrom(request.POST)
        if form.is_valid():