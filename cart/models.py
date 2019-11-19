from django.db import models
from user.models import *
from business.models import *

class Bill(details):
    email=models.CharField(max_length=200)
    date_purchase=models.DateField(editable=True)
    total_items=models.PositiveIntegerField()
    total_amt=models.DecimalField(max_digits=15 , decimal_places=2)
    
class item_purchased(details):
    item_id=models.ForeignKey(Stock , on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    #date_purchase=models.DateField(auto_now_add=True)


# Create your models here.
