from django.urls import path
from products.views import ProductView


urlpatterns = [
    path('', ProductView.as_view(), name='products'),

    path(
        '<int:product_id>/',
        ProductView.as_view(),
        name='product_detail'
    ),
]
