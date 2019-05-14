from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order, name="order"),
    path('exit/', views.exit, name="exit"),
    path('get_name/', views.get_name, name="get_name"),
    path('order_complete/', views.order_complete, name="order_complete"),
    path('order_side/', views.order_side, name="order_side"),
    path('order_side_only/', views.order_side_only, name="order_side_only"),
]