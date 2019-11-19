from django.urls import path
from . import views    
app_name='business'
urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('<int:pk>/', views.details,name="details"),
    path('edit/<int:pk>/',views.edit,name="edit"),
    path('addnew/',views.addnew,name="addnew"),
    #path('delete/<int:pk>/',views.delete,name="delete")
    
]