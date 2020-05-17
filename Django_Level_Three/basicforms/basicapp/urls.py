from django.urls import path
from . import views

app_name = 'basicapp'

urlpatterns= [

    path('registration/',views.register,name='register'),
    

]
