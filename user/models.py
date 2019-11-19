from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class details(models.Model):
    name=models.CharField(max_length=200)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    address=models.CharField(max_length=500)

    class Meta:
        abstract=True

# Create your models here.
