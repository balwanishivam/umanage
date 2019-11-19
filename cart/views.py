from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import *
from .forms import *
from business.models import Stock 

total_itm=0
total_amunt=0
def addnew(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        print(dir(form))
        if form.is_valid():
            product = form.save(commit=True)
            form.save()

            # product = Product()
            # product.name = form.cleaned_data['name']
            # product.cetagory = form.cleaned_data['cetagory']
            # product.supplier = form.cleaned_data['supplier']
            # product.unit_price = form.cleaned_data['unit_price']
            # product.description = form.cleaned_data['description']
            # product.save()
            # return redirect('detail', pk=product.pk)
            return redirect('cart:index')
    else:
        form = BillForm()
    return render(request, 'cart/new.html', {'form': form})

#def addnew(request,item,amt):
#    if request.method == 'POST':
#        form = BillForm(request.POST)
#        print(dir(form))
#        if form.is_valid():
#            bill = form.save(commit=True)
#            form.save()
#
#            bill = Bill()
#            bill.name = form.cleaned_data['name']
#            bill.contact = form.cleaned_data['contact']
#            bill.address = form.cleaned_data['address']
#            bill.email = form.cleaned_data['email']
#            bill.date_purchase = form.cleaned_data['date_purchase']
#            bill.total_items = total_itm
#            bill.total_amt = total_amunt
#
#            bill.save()
#            #return redirect('detail', pk=bill.pk)
#            return redirect('cart:index')
#    else:
#        form = BillForm()
#    return render(request, 'cart/new.html', {'form': form})

def index(request):
    bills = Bill.objects.all()
    context = {'bills': bills}
    return render(request, 'cart/index.html', context)


def details(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    return render(request, 'cart/detail.html', {'bill': bill})
def checkout(request):
    return render(request, 'cart/checkout.html')
def check(request,name,quantity):
    product=Stock.objects.get(name=name)
    if product:
        if product.quantity>=quantity:
            product.quantity=product.quantity-quantity
            product.save()
            total_amunt=total_amunt+(product.selling_price*quantity)
            total_itm=total_itm+quantity
            return render(request,'cart/checkout.html',{'product':product})
        else:
            return render(request,'cart/checkout.html')
    else:
        return render(request,'cart/checkout.html')
# Create your views here.
