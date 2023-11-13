from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    path(f'item/', views.item, name='item')
]
