from rest_framework import serializers
from .models import City, Tour, Booking
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'country', 'locale')

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('id', 'title', 'desc', 'from_city', 'to_city', 'from_date', 'to_date', 'price')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'client', 'tour', 'status')