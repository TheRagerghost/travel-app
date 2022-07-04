from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import City, Tour, Booking
from django.contrib.auth.models import User
from .serializers import UserSerializer, BookingSerializer, CitySerializer, TourSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@api_view(('GET',))
@login_required
def view_my_profile(request):
    me : User = request.user
    return Response({'user': UserSerializer(me, many=False).data })

@api_view(('GET',))
def login_evelin(request):
    user = authenticate(request, username='evelin57', password='iamuser')
    if user is not None:
        login(request, user)
        return Response({'user': UserSerializer(request.user, many=False).data })
    else:
        return Response({'user': 'Not found.' })