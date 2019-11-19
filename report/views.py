from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from business.models import Stock
#from .forms import StockForm

def stockindex(request):
    products = Stock.objects.all()
    context = {'products': products}
    return render(request, 'report/index.html', context)
