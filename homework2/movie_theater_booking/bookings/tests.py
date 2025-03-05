from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Movie

# This will test the 3 models.
class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='marvelnerd421', password='iluvmarvel3')
        self.movie = Movie.objects.create(
            title='Avengers 5',
            description='The fifth movie in the famous series.',
            release_date=date(2025, 12, 4),
            duration=120
        )
        self.seat = Seat.objects.create(seat_number='22', is_booked=False)

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, 'Avengers 5')

    def test_booking_creation(self):
        booking = Booking.objects.create(movie=self.movie, seat=self.seat, user=self.user)
        self.assertEqual(booking.movie.title, 'Avengers 5')
        self.assertFalse(self.seat.is_booked)  

# This will test the API for the movie list.
class MovieAPITestCase(APITestCase):
    def setUp(self):
        self.movie_list_url = reverse('movie-list') 

    def test_get_movies(self):
        response = self.client.get(self.movie_list_url)
        self.assertEqual(response.status_code, 200)
