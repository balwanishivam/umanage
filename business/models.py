from django.db import models
from user.models import *



class StaffDetail(details):
    salary=models.DecimalField(max_digits=13, decimal_places=2)
    date_of_employment=models.DateField(auto_now_add=True)
    job_profile=models.CharField(max_length=200)

class Stock(models.Model):
    name=models.CharField(max_length=100)
    ptype=models.CharField(max_length=100)
    dealer_name=models.CharField(max_length=200)
    dealer_id=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    cost_price=models.DecimalField(max_digits=13,decimal_places=2)
    selling_price=models.DecimalField(max_digits=13,decimal_places=2)

class businessdetail(details):
    no_of_staff=models.PositiveIntegerField()





# Create your models here.
