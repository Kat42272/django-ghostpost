from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpost_app.models import Post
from ghostpost_app.forms import PostForm



def index(request):
  posts = Post.objects.all().order_by('-postDate')
  return render(request, 'index.html', {"posts":posts})


def boasts(request):
  posts = Post.objects.filter(isBoast=True).order_by('-postDate')
  return render(request, 'index.html', {"posts":posts})


def roasts(request):
  posts = Post.objects.filter(isBoast=False).order_by('-postDate')
  return render(request, 'index.html', {"posts":posts})


def sorted(request):
  posts = Post.objects.order_by('-postDate')
  return render(request, 'index.html', {"posts":posts})


def add_post_view(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      Post.objects.create(
        isBoast=data['post_choices'],
        body=data['post'],
        upVotes=0,
        downVotes=0,
      )
      return HttpResponseRedirect(request.GET.get('next', reverse('home')))
  form = PostForm()
  return render(request, 'generic_form.html', {'form': form})


def upVote(request, id):
  post = Post.objects.get(id=id)
  post.upVotes += 1
  post.save()
  return HttpResponseRedirect(reverse('home'))


def downVote(request, id):
  post = Post.objects.get(id=id)
  post.downVotes += 1
  post.save()
  return HttpResponseRedirect(reverse('home'))

