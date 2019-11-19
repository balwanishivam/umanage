from django import forms
from .models import Stock

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('name', 'ptype', 'dealer_name','dealer_id', 'quantity','cost_price', 'selling_price')
