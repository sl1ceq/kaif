from django.urls import path
from . import views



urlpatterns = [
    path('', views.main, name='main'),
    path('order_create/', views.order_create, name='order_create'),
    path('order_created/', views.ordered, name='order_created')
]