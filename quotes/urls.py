 
from django.urls import path, include

from quotes.views import (
    create_quotes,
    view_quotes,
    edit_quotes,
    delete_quotes
)

app_name='quotes'

urlpatterns = [
    path('create', create_quotes, name='create'),
    path('view', view_quotes, name='view'),
    path('<id>/edit', edit_quotes, name='edit'),
    path('<id>', delete_quotes, name='delete') 
]