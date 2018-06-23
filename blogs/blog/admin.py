from django.contrib import admin

# Register your models here.
from .models import Category,Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modified_time','category','auther']
admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)