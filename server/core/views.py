from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from .models import City, Tour, Booking
from django.contrib.auth.models import User
from .serializers import UserSerializer, BookingSerializer, CitySerializer, TourSerializer
from .paginations import SmallSetPagination
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityViewSetPaginated(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = SmallSetPagination

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@api_view(('GET',))
def view_my_profile(request):
    me : User = request.user
    bookings = Booking.objects.filter(Q(client_id=me.pk))
    bk_reply = BookingSerializer(bookings, many=True).data

    return Response({'user': UserSerializer(me, many=False).data, 'bookings' : bk_reply})

@api_view(('GET',))
def users_filtered(request):
    get = request.GET.get('gender','')
    users = User.objects.filter()
    if get is 'M' or 'F':
        users = users.filter(Q(last_name=get))
        return Response({'user': UserSerializer(users, many=True).data })
    else:
        return Response({'users': 'Wrong request.' })

@api_view(('GET',))
def login_raw(request):
    username = request.GET.get('username','')
    password = request.GET.get('password','')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        bookings = Booking.objects.filter(Q(client_id=user.pk))
        bk_reply = BookingSerializer(bookings, many=True).data

        return Response({'user': UserSerializer(user, many=False).data, 'bookings' : bk_reply})
    else:
        return Response({'user': 'Not found.' })

@api_view(('GET',))
def logout_raw(request):
    logout(request)
    return Response({'user': 'Logged out.' })