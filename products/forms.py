from django.forms import ModelForm
from products.models import Product

class ProductFrom(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'