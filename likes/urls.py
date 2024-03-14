from django.urls import path
from .views import like, demo

app_name = 'likes'
urlpatterns = [
    path('demo/', demo, name='demo'),
    path('', like, name='like'),
]
