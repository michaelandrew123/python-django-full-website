from django import forms
from quotes.models import Qoutes


class CreateQuotesForm(forms.ModelForm):

    class Meta:
        model = Qoutes
        fields = ['title', 'description', 'category']



class UpdateQuotesForm(forms.ModelForm):

    class Meta:
        model = Qoutes
        fields = ['title', 'description', 'category']

    def save(self, commit=True):
        quotes_update=self.instance
        quotes_update.title = self.cleaned_data['title']
        quotes_update.description = self.cleaned_data['description']
        quotes_update.category = self.cleaned_data['category']

        if commit:
            quotes_update.save()
        return quotes_update
