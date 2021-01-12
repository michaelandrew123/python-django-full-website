from django.shortcuts import render
from personal.models import Question
from account.models import Account

# Create your views here.
def home_screen_view(request):
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, './home.html', context)

def user_account(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request, './accounts.html', context)
    