from django.contrib import admin
from blog.models import Blogpost,NewBlog,BlogComment
# Register your models here.

admin.site.register(Blogpost)
admin.site.register(NewBlog)
admin.site.register(BlogComment)