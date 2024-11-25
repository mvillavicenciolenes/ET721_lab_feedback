from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('item/<int:pk>/', views.item_detail, name='item_detail'),  # Item detail page
]
