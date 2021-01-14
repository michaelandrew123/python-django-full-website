from django.urls import path, include
from blog.views import (
    create_blog_view,
)


app_name = 'blog'

urlpatterns = [
    path('create', create_blog_view, name='create'),

]