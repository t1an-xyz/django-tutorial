import django_filters
from django_filters import DateFilter
from django import forms
from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = DateFilter(field_name='date_created', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']