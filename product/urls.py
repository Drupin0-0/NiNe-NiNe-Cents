from django.urls import path
from . import views

urlpatterns = [
    path ('register/', views.product_register, name='product_register')
]