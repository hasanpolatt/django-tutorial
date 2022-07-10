from django.urls import path
from . import views

urlPatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.single, name='single')
]