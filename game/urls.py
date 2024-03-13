from django.urls import path
from . import views


app_name = 'game'

urlpatterns = [
    path('start/', views.game_start, name='game_start'),
    path('play/', views.game_play, name='game_play'),
]
