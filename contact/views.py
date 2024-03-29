from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.

def init(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'contact/contact.html',{'posts':post})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'contact/post_detail.html',{'post':post})