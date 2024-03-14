from django.views.generic import TemplateView

from django.shortcuts import render
from likes.models import LikeCounter


class Homepage(TemplateView):
    template_name = 'index.html'


def index(request):
    likes_count = LikeCounter.objects.first()
    context = {'likes_count': likes_count}
    return render(request, 'index.html', context)


class Aboutpage(TemplateView):
    template_name = 'about.html'
