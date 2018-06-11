from django.urls import path
from blog import views
from django.conf.urls import handler404,handler500

app_name='blog'
urlpatterns = [
    path('',views.blog_index,name='index'),
    path('<int:blog_id>/',views.blog_xiangqing,name='xiangqing'),
    path('fabu',views.blog_fabu,name='fabu'),
]

handler404 = views.error
handler500 = views.error
