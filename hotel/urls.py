from django.urls import path, include
from .views import (
    hotel_image_view,
    success_msg,
    display_hotel_images,
    place_,
    place_edit,
    place_delete,
    restaurant_,
)

app_name="hotel"


urlpatterns = [ 
    path('image_upload/', hotel_image_view, name = 'image_upload'), 
    path('success/', success_msg, name = 'success'), 
    path('hotel_images/', display_hotel_images, name = 'hotel_images'),
    path('place/', place_, name="place"),
    path('<id>/edit', place_edit, name="edit"),
    path('<id>', place_delete, name="delete"),
    path('restaurant/', restaurant_, name="restaurant") 
]

