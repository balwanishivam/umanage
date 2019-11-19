from django.urls import path
from . import views
# SET THE NAMESPACE!
app_name = 'accounts'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('',views.home,name="home"),
    path('index/',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout',views.user_login,name='logout'),
    #url(r'^register/$',views.register,name='register'),
    #url(r'^user_login/$',views.user_login,name='user_login'),
]