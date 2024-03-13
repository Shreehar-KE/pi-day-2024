from django.urls import path
from . import views


app_name = 'facts'
urlpatterns = [
    path('', views.random_fact, name='fact'),
    path('add/', views.add_facts, name='add_facts'),
]
