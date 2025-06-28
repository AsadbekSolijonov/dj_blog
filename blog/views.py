import random
from dataclasses import dataclass

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import BlogForms, CustomUserCreationForm
from blog.models import Blog


@login_required
def home(request):
    blog = Blog.objects.filter(is_active=True)

    search = request.GET.get('active_query')
    if search:
        blog = Blog.objects.filter(title__icontains=search, is_active=True)

    context = {
        "blogs": blog
    }
    return render(request, template_name='blog/home.html', context=context)


@login_required
def in_active(request):
    blog = Blog.objects.filter(is_active=False)

    search = request.GET.get('in_active_query')
    if search:
        blog = Blog.objects.filter(title__icontains=search, is_active=False)

    context = {
        "blogs": blog
    }
    return render(request, template_name='blog/in_active.html', context=context)


def about(request):
    context = {
    }
    return render(request, template_name='blog/about.html', context=context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        "blog": blog
    }
    return render(request, template_name='blog/detail.html', context=context)


def update(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForms(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            messages.success(request, message=f"{blog.title} o'zgartirildi!")
            if blog.is_active:
                return redirect('home')
            return redirect('in_active_blogs')
    else:
        form = BlogForms(instance=blog)
    context = {
        "form": form,
        "blog": blog
    }
    return render(request, 'blog/update.html', context=context)


def delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = BlogForms(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, message=f"{blog.title} yaratildi!")
            return redirect('home')
    else:
        messages.warning(request, message=f"Hozirda biz test rejimida ishlayapmiz!")
        form = BlogForms()

    context = {
        "form": form
    }
    return render(request, 'blog/create_blog.html', context=context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, message=f"{user.username} username li foydalanuvchi yaratildi!")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form
    }
    return render(request, 'blog/register.html', context=context)


def site_logout(request):
    logout(request)
    return redirect('ask_login')


def ask_login(request):
    return render(request, 'blog/logout.html')
