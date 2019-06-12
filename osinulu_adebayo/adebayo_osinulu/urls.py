from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('contact_me', views.contact_me, name='contact_me'),
    
]
