from django.contrib import admin
from .models import City, Tour, Booking

# Register your models here.

admin.site.register(City)
admin.site.register(Tour)
admin.site.register(Booking)