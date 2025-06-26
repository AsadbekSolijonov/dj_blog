import random
from dataclasses import dataclass

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import BlogForms
from blog.models import Blog


@dataclass
class Students:
    first_name: str
    last_name: str
    phone: str
    payed: bool


st1 = Students('Alisher', 'Eshmatov', '998 91 903 34-43', True)
st2 = Students('Alex', 'Gorden', '998 91 903 34-43', False)
st3 = Students('Avazbek', 'Boymuradov', '998 90 903 00-42', True)
st4 = Students('Abror', 'Sotiboldiyev', '998 33 300 40-43', True)
students = [st1, st2, st3, st4]


def home(request):
    blog = Blog.objects.filter(is_active=True)

    search = request.GET.get('active_query')
    if search:
        blog = Blog.objects.filter(title__icontains=search, is_active=True)

    context = {
        "blogs": blog
    }
    return render(request, template_name='blog/home.html', context=context)


def in_active(request):
    context = {
        "blogs": Blog.objects.filter(is_active=False)
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
            return redirect('home')
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
