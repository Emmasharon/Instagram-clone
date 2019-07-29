from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile,Post,Following,Comment,User
from .forms import ProfileForm,PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import F


def index(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    posts=Post.objects.all()
    current_user = request.user
    following=Following.objects.filter(username=current_user.username).all()
    numberfollowing=len(following)
    followers=Following.objects.filter(followed=request.user.username).all()
    numberfollower=len(followers)
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES)
        if profileform.is_valid():
            profile = profileform.save(commit=False)
            profile.user = current_user
            profile.save()
            
        return redirect('profile')

    else:
        profileform = ProfileForm()
        
    return render(request, 'profile.html',locals())

@login_required(login_url='/accounts/login/')
def new_post(request):
    posts=Post.objects.all()
    current_user = request.user
    following=Following.objects.filter(username=current_user.username).all()
    numberfollowing=len(following)
    followers=Following.objects.filter(followed=request.user.username).all()
    numberfollower=len(followers)
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.profile = current_user.profile
            post.save()

        return redirect('new_post')

    else:
        postform = PostForm()
    
    return render(request, 'new_post.html', locals())

@login_required(login_url='/accounts/login/')
def timeline(request):
    users = User.objects.all()
    posts = Post.objects.all()
    follows = Following.objects.all()
    comments = Comment.objects.all()
    # if request.method=='POST' and 'follow' in request.POST:
    #     following=Following(username=request.POST.get("follow"),followed=request.user.username)
    #     following.save()
    #     return redirect('timeline')
    # elif request.method=='POST' and 'comment' in request.POST:
    #     comment=Comment(comment=request.POST.get("comment"),
    #                     post=int(request.POST.get("posted")),
    #                     username=request.POST.get("user"),
    #                     count=0)
    #     comment.save()
    #     comment.count=F('count')+1
    #     return redirect('timeline')
    # elif request.method=='POST' and 'post' in request.POST:
    #     posted=request.POST.get("post")
    #     for post in posts:
    #         if (int(post.id)==int(posted)):
    #             post.like+=1
    #             post.save()
    #     return redirect('timeline')
    #     print (posts)
    # else:
    return render(request, 'timeline.html',locals())