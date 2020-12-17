from django.urls import path
from blog import views
urlpatterns = [
    path('blogComment/',views.blogComment),
    path('search/',views.search),
    path('myblog/',views.myblog),
    path('',views.blog),
    path('newblog/',views.newblog),
    path('read/<int:ed>/',views.readblog),
    
]
