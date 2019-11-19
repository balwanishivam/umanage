from django.urls import path
from . import views    
app_name='cart'
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:pk>/', views.details,name="details"),
    #path('edit/<int:pk>/',views.edit,name="edit"),
    path('addnew/',views.addnew,name="addnew"),
    #path('addnew/<name>/<int:quantity>',views.addnew,name="addnew"),
    #path('checkout/',views.checkout,name="checkout"),
    #path('<product>/<int:quantity>/',views.check,name="check")
    #path('delete/<int:pk>/',views.delete,name="delete")
    
]