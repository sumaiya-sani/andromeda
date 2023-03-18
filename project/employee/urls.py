from django.urls import path
from employee import views
from . import views



urlpatterns = [
   
    path('home/',views.home,name='home' ),
    path('index/',views.home_withQ,name='home_question' ),

    


]
