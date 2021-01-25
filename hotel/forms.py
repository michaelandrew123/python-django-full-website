from django import forms
from .models import *


class HotelForm(forms.ModelForm): 
    class Meta: 
        model = Hotel 
        fields = ['name', 'hotel_Main_Img'] 


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

class WaiterForm(forms.ModelForm):
    class Meta:
        model = Waiter
        fields = '__all__'
