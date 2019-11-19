from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Stock
from .forms import StockForm

def index(request):
    products = Stock.objects.all()
    context = {'products': products}
    return render(request, 'business/index.html', context)

def home(request):
    return render(request, 'business/home.html')

def details(request, pk):
    product = get_object_or_404(Stock, pk=pk)
    return render(request, 'business/detail.html', {'product': product})


def addnew(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()

            # product = Product()
            # product.name = form.cleaned_data['name']
            # product.cetagory = form.cleaned_data['cetagory']
            # product.supplier = form.cleaned_data['supplier']
            # product.unit_price = form.cleaned_data['unit_price']
            # product.description = form.cleaned_data['description']
            # product.save()
            # return redirect('detail', pk=product.pk)
            return redirect('business:index')
    else:
        form = StockForm()
    return render(request, 'business/new.html', {'form': form})


def edit(request, pk):
    product = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('business/index')
    else:
        form = StockForm(instance=product)
    return render(request, 'business/edit.html', {'form': form})

#def delete(request,pk):
#def search(request,product):
#
