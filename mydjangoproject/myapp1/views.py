from django.shortcuts import render
from myapp1.models import SalesOrder
from rest_framework.viewsets import ModelViewSet
from myapp1.serializers import OrderSerializer

def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})

class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer

def orders_page(request):
    return render(request, 'main_app.html',)