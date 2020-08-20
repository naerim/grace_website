from django.shortcuts import render, redirect
from .models import Post, Category
from django.views.generic import ListView, DetailView
from django.contrib import auth


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        return context


class PostListByCategory(ListView):

    def get_queryset(self):
        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)
        context['category'] = category

        return context


def index(request):
    posts = Post.objects.all()

    return render(
        request,
        'grace/main.html',
        {
            'posts': posts,
        }
    )


def logout(request):
    auth.logout(request)
    return redirect('../')


def myPage(request):
    return render(request, 'grace/myPage.html')


def tutor(request):
    return render(request, 'grace/tutor.html')


def introduce(request):
    return render(request, 'grace/introduce.html')


def apply(request):
    return render(request, 'grace/apply.html')
