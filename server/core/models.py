from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField('name', max_length=50)
    country = models.CharField('country', max_length=20, blank=True, null=True)
    locale = models.CharField('locale', max_length=6, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Tour(models.Model):
    title = models.CharField('title', max_length=50)
    desc = models.TextField('description')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city', blank=True, null=True)
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city', blank=True, null=True)
    from_date = models.DateField('from_date')
    to_date = models.DateField('to_date')
    price = models.FloatField('price')

    def __str__(self) -> str:
        return self.title

class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    book_date = models.DateTimeField('book_date')
    status = models.CharField('status', max_length=50)

    def __str__(self) -> str:
        return '%s / %s <-> %s / %s' % (self.client.first_name, self.tour.from_city, self.tour.to_city, self.book_date)
