from aiohttp import request
from django.db import router
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'cities', CityViewSet)
router.register(r'tours', TourViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]