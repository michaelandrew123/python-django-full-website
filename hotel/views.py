from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here. 
def hotel_image_view(request):   
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
 
    return render(request, 'index.html', {'form' : form}) 
  
  
def success_msg(request): 
    return HttpResponse('successfully uploaded') 
    

# Python program to view  
# for displaying images 
  
def display_hotel_images(request):  
    if request.method == 'GET':  
        # getting all the objects of hotel. 
        Hotels = Hotel.objects.all()  
        return render(request, 'view_hotel.html', 
                     {'hotel_images' : Hotels})


def place_(request): 
    context = {} 
    if request.POST:    
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            context['msg_'] = "Success adding places!"
    
    else: 
        form = PlaceForm() 
        context['place_form'] = form
    

    view_place = Place.objects.all()
    context['view_places'] = view_place

    return render(request, 'place/index.html', context)

def place_edit(request, id):
    return render(request, 'place/index.html', {})


def place_delete(request, id):
    return render(request, 'place/index.html', {})


def restaurant_(request):
    context = {} 

    if request.POST:
        form = RestaurantForm(request.POST or None)
        if form.is_valid():
            form.save()
            context['msg_'] = "Success adding info!"
    else:
        form = RestaurantForm()
        context['restaurant_form'] = form
            
 
    place_form = Place.objects.all()
    context['placeform'] = place_form 

    view_restaurant = Restaurant.objects.all()
    context['view_restaurant'] = view_restaurant 


    

    return render(request, 'restaurant/r_index.html', context)

