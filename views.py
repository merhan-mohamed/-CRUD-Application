

# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostModelForm
from .models import Post, Author


#list of posts
def post_list(request):
    all_posts = Post.objects.all()
    context ={
        'all_posts' : all_posts
    }
    messages.info(request, 'Here are all the current blog posts')
    return render(request, 'post_list.html', context)

#retrieve posts
def post_details(request, slug):
    unique_post=get_object_or_404(Post,slug=slug)
    context = {
        'post': unique_post
    }
    messages.info(request,'This is the specific detail view')
    return render(request, 'post_details.html', context)
#create posts
#@login_required
def posts_create(request):
    author, created = Author.objects.get_or_create(
         user=request.user,
         email = request.user.email,
         cellphone=8235214
     )
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
        messages.info(request, 'Successfully created a new blog post!')
        return redirect('/project5/')
    context = {'form': form}
    return render(request, 'post_create.html', context)
#update posts
def posts_update(request,slug):
    #unique_post = get_object_or_404(Post,slug=slug)
    form = PostModelForm(request.POST or None, request.FILES or None)
    if request.method == Post:
        if form.is_valid():
           form.save()
           return redirect('/project5/')
    else:
        form = PostModelForm()
    context = {'form': form}
    messages.info(request, 'Successfully updated your blog post.')
    return render(request, 'post_update.html', context)
# delete posts
def post_delete(request,slug):
    unique_post = get_object_or_404(Post,slug)
    unique_post.delete()
    messages.info(request, 'Successfully deleted blog post.')
    return redirect('/project5/')






