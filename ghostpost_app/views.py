from django.shortcuts import render

def ghost_post_view(request):
  return render(request, 'index.html', {})


def add_post_view(request):
  return render(request, 'add_post.html', {})


def boasts_view(request):
  return render(request, 'boasts.html', {})


def roasts_view(request):
  return render(request, 'roasts.html', {})


def sorted_by_time_view(request):
  return render(request, 'sorted.html', {})