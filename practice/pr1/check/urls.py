from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('display',views.display,name='display'),
    path('edit',views.edit,name="edit"),
    path('product/<int:product_id>/order/', views.process_order, name='process_order'),
]