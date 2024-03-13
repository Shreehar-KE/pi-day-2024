from django.urls import path
from .views import Homepage, Aboutpage

app_name = 'core'
urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('about/', Aboutpage.as_view(), name='about'),
]
