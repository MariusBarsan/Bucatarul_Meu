from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from ganduri.forms import CommentForm
from ganduri.models import Post, Category


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status = Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)

    else:
        form = CommentForm()


    form = CommentForm()

    return render(request, 'ganduri/detail.html', {'post': post, 'form': form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'ganduri/category.html', {'category': category, 'posts': posts})


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'ganduri/search.html', {'posts': posts, 'query': query})