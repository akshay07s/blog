from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blogpost,NewBlog,BlogComment
from datetime import date
from django.contrib import messages
from django.contrib.auth.admin import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def blog(request):
    if User.is_authenticated:
        posts= Blogpost.objects.all()
        param={'posts':posts}
        return render(request,'blog/blogpost.html',param)
    else:
        return HttpResponse("page not found")
@login_required
def readblog(request,ed):

    readpost=Blogpost.objects.filter(post_id=ed).first()
    comment=BlogComment.objects.filter(post=readpost)
    context={'readpost':readpost,'comment':comment}
    return render(request,'blog/readblog.html',context)
@login_required
def blogComment(request):
    if request.method=='POST':
        comment=request.POST.get('comment')
        user=request.user
        postId=request.POST.get('postId')
        post=Blogpost.objects.get(post_id=postId)
        if comment=='' or len(comment)==0:
            messages.error(request,'comment cant be blank')
            return redirect(f'/blog/read/{postId}')
        comment=BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,'Successfully submited')
    return redirect(f'/blog/read/{postId}')
@login_required
def newblog(request):
    if request.method=='POST':
        title =request.POST['title1']
        desc =request.POST['desc1']
        name =request.POST['name1']
        image=request.FILES.get('image1')
        date1=date.today()
        post_input =Blogpost(title=title,desc=desc,name=name,date=date1,image=image)
        post_input.save()
        messages.success(request,'successfully submitted')
    return render(request,'blog/newblog.html')
@login_required
def search(request):
    search=request.GET['search']
    allpost=Blogpost.objects.filter(title__icontains=search)
    params={'allpost':allpost,'search':search}
    return render(request,'blog/search.html',params)
@login_required
def myblog(request):
    myblog=Blogpost.objects.filter(name=request.user)
    params={'myblog':myblog}
    return render(request,'blog/myblog.html',params)