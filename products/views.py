from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser

from products.models import Product
from products.serializers import ProductSerializerV3


class ProductView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

        return [IsAdminUser()]

    def get(self, request, product_id=None):

        if product_id:
            product = get_object_or_404(
                Product,
                id=product_id
            )

            serializer = ProductSerializerV3(product)
            return Response(serializer.data)

        products = Product.objects.all()
        serializer = ProductSerializerV3(products, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = ProductSerializerV3(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, product_id):

        product = get_object_or_404(
            Product,
            id=product_id
        )

        serializer = ProductSerializerV3(
            product,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, product_id):

        product = get_object_or_404(
            Product,
            id=product_id
        )

        serializer = ProductSerializerV3(
            product,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, product_id):

        product = get_object_or_404(
            Product,
            id=product_id
        )

        product.delete()

        return Response(
            {'message': 'Product deleted successfully'},
            status=status.HTTP_200_OK
        )