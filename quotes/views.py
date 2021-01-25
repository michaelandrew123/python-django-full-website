from django.shortcuts import render, redirect, get_object_or_404
from quotes.models import Qoutes
from django.contrib.auth import authenticate
from quotes.forms import CreateQuotesForm, UpdateQuotesForm
from account.models import Account
from django.http import HttpResponse
# Create your views here.

def create_quotes(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('must-authenticate')
    context = {}


    categories = CreateQuotesForm
             
    context['categories'] = categories

    form = CreateQuotesForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateQuotesForm()
        return redirect('quotes:view')


    context['form'] = form

    return render(request, 'create.html', context)

def view_quotes(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must-authenticate')
    

    #   blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    quotes = Qoutes.objects.order_by('-id')
    context['quotes'] = quotes

    return render(request, 'view.html', context)


def edit_quotes(request, id):
    context={}

    user = request.user

    if not user.is_authenticated:
        return redirect('must-authenticate')
    categories = CreateQuotesForm 
    context['categories'] = categories

    quotes_update = get_object_or_404(Qoutes, id=id)

    if quotes_update.author != user:
        return HttpResponse('You are not the author of that quotes. ')

    if request.POST:
        form = UpdateQuotesForm(request.POST or None, instance=quotes_update)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message']  = "Updated" 
            quotes_update = obj

    form = UpdateQuotesForm(
        initial={
            "title": quotes_update.title,
            "description": quotes_update.description,
            "category": quotes_update.category
        }
    )

 
    context['form'] = form

    return render(request, 'edit.html', context)

    
def delete_quotes(request, id):
    user = request.user 
    context = {}
    if not user.is_authenticated:
        return redirect('must-authenticate')

    quotes_delete = get_object_or_404(Qoutes, id=id)
    if quotes_delete.author != user:
        return HttpResponse('You are not the author of that quotes!')

    delete = Qoutes.objects.filter(id=id).delete() 

    # instance = Qoutes.objects.get(id=id)
    # instance.delete()
    if delete: 
        context['success_message'] = "Quotes deleted ID:" + id
    
    return redirect('quotes:view')