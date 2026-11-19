from rest_framework.views import APIView
from django.http import JsonResponse
from products.models import Product
from products.forms import ProductFrom


class ProductView(APIView):

    def get(self, request):
        products = Product.objects.all().values('name', 'price')
        return JsonResponse(list(products), safe=False)

    def post(self, request):
        form = ProductFrom(request.data)

        if form.is_valid():
            form.save()
            return JsonResponse({'result': 'okay'})

        return JsonResponse(
            {'error': form.errors.get_json_data()},
            status=400
        )