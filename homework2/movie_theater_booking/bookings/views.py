from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.contrib import messages

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
# This view is for the home page, listing all of the movies.
def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

# This view is for the page of viewing the seat booking. If you book the seat and it is available, it will take you back to the home page and display that you got it.
# If not, it take you to the home page and say that it is already taken.
def seat_booking_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()

    if request.method == 'POST':
        seat_number = request.POST.get('seat_number')
        seat = get_object_or_404(Seat, seat_number=seat_number)

        if not seat.is_booked:
            # Mark seat as booked
            seat.is_booked = True
            seat.save()
            # Create a booking record
            Booking.objects.create(movie=movie, seat=seat, user=request.user)
            # Show success message
            messages.success(request, f"You have booked seat {seat_number} for {movie.title}!")
        else:
            # Show an error or warning if seat is already taken
            messages.warning(request, f"Seat {seat_number} is already taken.")

        # Redirect to movie listing page (assuming you have a URL named 'movie_list')
        return redirect('movie_list')

    # If GET request, just render the seat booking page
    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats,
    })

# This view is for the booking history page.
def booking_history_view(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': user_bookings})


