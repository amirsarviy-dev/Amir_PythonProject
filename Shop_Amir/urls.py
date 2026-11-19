from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', include('products.urls')),

    path('users/', include('users.urls')),

    path('cart/', include('carts.urls')),

    path('orders/', include('orders.urls')),

    path('api/token/', TokenObtainPairView.as_view()),

    path('api/token/refresh/', TokenRefreshView.as_view()),
]

