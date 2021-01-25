from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from personal.models import Question
from account.models import Account
from blog.models import BlogPost
from blog.views import get_blog_queryset
from operator import attrgetter

BLOG_POSTS_PER_PAGE = 10

# Create your views here.
def home_screen_view(request):
    context = {}
    # questions = Question.objects.all()
    # context['questions'] = questions

    query = ''
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
     
    #Pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)
    
    context['blog_posts'] = blog_posts

    return render(request, './home.html', context)

def user_account(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request, './accounts.html', context)


