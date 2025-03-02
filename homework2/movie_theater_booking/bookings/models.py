from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    releaseDate = models.DateField()
    duration = models.IntegerField()

class Seat(models.Model):
    seatNumber = models.CharField(max_length=255)
    isBooked = models.BooleanField(default=False)

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookingData = models.DateTimeField(auto_now_add=True)