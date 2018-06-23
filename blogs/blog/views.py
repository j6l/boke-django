from django.shortcuts import render

# Create your views here.
from . models import Article

def index(request):
    article_list = Article.objects.all().order_by('-create_time')
    return render(request,'blog/index.html',context={'article_list':article_list})
