from django.shortcuts import render, render_to_response
from blog.models import BlogsPost

# Create your views here.
def blog_index(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request,'index.html', {'blog_list':blog_list})   # 返回index.html页面

def blog_xiangqing(request,blog_id):
    blogli = BlogsPost.objects.get(pk=blog_id)
    return render( request, 'xiangqing.html',{'blogli':blogli} )

def blog_fabu(request):
    if request.method == 'POST':
        titles = request.POST['title']
        bodys = request.POST['body']
        BlogsPost.objects.create(title=titles,body=bodys)
    return render(request,'fabu.html')

def error(request):
    return render_to_response( '404.html' )
