from django.shortcuts import render, redirect
from .models import LikeCounter
from django.http import JsonResponse, Http404


def demo(request):
    if not request.user.is_authenticated:
        raise Http404
    likes_count = LikeCounter.objects.first()
    context = {'likes_count': likes_count}
    return render(request, 'like_demo.html', context)


def like(request):
    if request.method == 'POST':
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        if 'liked' not in request.session:
            like_counter = LikeCounter.objects.first()
            like_counter.likes += 1
            like_counter.save()
            request.session['liked'] = True
            return JsonResponse({'likes': like_counter.likes})
        else:
            return JsonResponse({'error': 'Already liked'}, status=400)
    return redirect('/')
