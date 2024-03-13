from django.shortcuts import render, redirect
from .models import Fact
from .forms import FactForm
from django.contrib import messages
from django.http import Http404
import csv
import random


def random_fact(request):
    facts = Fact.objects.all()
    if facts:
        random_fact = random.choice(facts)
    else:
        random_fact = None
    context = {'random_fact': random_fact}
    return render(request, 'facts.html', context)


def add_facts(request):
    if not request.user.is_authenticated:
        raise Http404
    if request.method == 'POST':
        form = FactForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES.get('csv_file')
            if csv_file:
                try:
                    decoded_file = csv_file.read().decode('utf-8').splitlines()
                    reader = csv.reader(decoded_file)
                    for row in reader:
                        fact = row[0]
                        Fact.objects.create(fact=fact)
                    messages.success(request, 'Facts imported successfully!')
                except Exception as e:
                    messages.error(
                        request, f'Error importing facts from CSV: {e}')
            return redirect('facts:fact')
    else:
        form = FactForm()
    return render(request, 'add_facts.html', {'form': form})
