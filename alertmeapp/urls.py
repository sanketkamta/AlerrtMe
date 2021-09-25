from django.urls import path
from alertmeapp import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('thankyou/',views.thankyou, name='thankyou'),
]