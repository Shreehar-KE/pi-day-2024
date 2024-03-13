from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player
import json


def game_start(request):
    players = Player.objects.all()
    context = {'players': players}
    return render(request, 'game_start.html', context)


def game_play(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        location = data.get('location')
        score = data.get('score')

        new_player = Player(name=name, location=location, score=score)
        # notify admin
        new_player.save()
        return redirect('game:game_start')

    return render(request, 'game_play.html')
