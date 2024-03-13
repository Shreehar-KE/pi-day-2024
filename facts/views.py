from django.shortcuts import render
import random

from .models import Fact
# Create your views here.


def random_fact(request):
    facts = Fact.objects.all()
    if facts:
        random_fact = random.choice(facts)
    else:
        random_fact = None
    context = {'random_fact': random_fact}
    return render(request, 'facts.html', context)
