from django.urls import path
from .views import index, Aboutpage

app_name = 'core'
urlpatterns = [
    path('', index, name='index'),
    path('about/', Aboutpage.as_view(), name='about'),
]
