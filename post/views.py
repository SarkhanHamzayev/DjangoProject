from django.shortcuts import render, HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.utils.text import  slugify

# Create your views here.


def post_index(request):
    posts =Post.objects.all()
    return render(request,'post/index.html', {"posts": posts})

def post_detail(request,slug):
    post=get_object_or_404(Post,slug=slug)
    return render(request,'post/detail.html',{"post": post})

def post_create(request):


    # if request.method=="POST":
    #     print(request.POST)

    # title= request.POST.get('title')
    # content= request.POST.get('content')
    # Post.objects.create(title=title,context=context)

    # if request.method =='POST':
    #     #Formdan gelen melumatlari qeyd et
    #     form =PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     #Formu istifadeciye goster
    #     form = PostForm()

    form=PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # post=form.save(commit=False)
        # post.slug=slugify(post.title.replace('ı','i'))
        # post.save()
        post = form.save()
        messages.success(request,"Basarili bir sekilde olusturdunuz", extra_tags="mesaj-info")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request,'post/form.html',context)

def post_update(request,slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Basarili bir sekilde update edildi")
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'post/form.html', context)

def post_delete(request,slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')