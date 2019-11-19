from django import forms
from .models import *

class BillForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = ('name','contact','address','email','date_purchase','total_items','total_amt')

class PurchasedForm(forms.ModelForm):
    class Meta:
        model=item_purchased
        fields=('name','contact','address','item_id','quantity')