from django.urls import path
from .views import home_view, hotel_list_view, booking_confirm_view, hotel_search_ajax_view

urlpatterns = [
    path('', home_view, name='home'),
    path('search/', hotel_list_view, name='hotel_search'),
    path('booking/confirm/', booking_confirm_view, name='booking_confirm'),
    path('search-ajax/', hotel_search_ajax_view, name='hotel_search_ajax'), # 👈 これを追記
]