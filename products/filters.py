import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    # name=django_filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = Product
        fields = {
            'name':['icontains'],
            'price':['lt', 'gt'],
        }