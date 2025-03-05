from django.urls import path, include
from rest_framework import routers
from . import views
from .views import MovieViewSet, SeatViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.movie_list_view, name='movie_list'),
    path('movies/<int:movie_id>/seats/', views.seat_booking_view, name='seat_booking'),
    path('bookings/history/', views.booking_history_view, name='booking_history'),
    
]