from django.shortcuts import render, redirect, get_object_or_404
from .forms import Postform, Commentform
from .models import Post
from django.utils import timezone

def home(request):
    #Posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date')
    return render(request,'index.html', {'posts': posts})

# def postcreate(request):
#     if request.method == 'POST' or request.method == 'FILES':
#         form = Postform(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = Postform()
#     return render(request, 'post_form.html')

def new(request):
    return render(request,'new.html')

def create(request):
    if(request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        user = request.user
        
        post.save()
    return redirect('home')

    

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form= Commentform()
    return render(request, 'detail.html',{'post_detail':post_detail,'comment_form':comment_form})

def new_comment(request, post_id):
    filled_form=Commentform(request.POST)
    if filled_form.is_valid():
        finished_form=filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('detail',post_id)

def freehome(request):
    return