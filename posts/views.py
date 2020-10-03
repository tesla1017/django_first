from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    #return HttpResponse("Hello, World!")
    posts = Post.objects.order_by('-published') #models.pyのPostクラスの内容を取得し、投稿日でソートしてpostsに格納
    return render(request, 'posts/index.html', {'posts': posts}) #レンダリング
