from django.urls import path
from . import views    

app_name='report'

urlpatterns = [
    path('stockindex/',views.stockindex,name="index"),
     
]