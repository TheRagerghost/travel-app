from datetime import datetime, timedelta
from django.utils import timezone
from random import randint, randrange
import random
from secrets import randbits
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from core.models import City, Tour, Booking

locales = ['en_US', 'de_DE', 'en_GB', 'fr_FR']
Faker.seed(randint(0, 999999))


class Command(BaseCommand):
    help = 'Fills database with cities, tours and bookings'

    def add_arguments(self, parser) -> None:
        parser.add_argument('count', type=int, nargs='?', default=20)

    def handle(self, *args, **options):

        if User.objects.all().count() < 5:
            self.stdout.write(self.style.WARNING('Not enough users in the database!'))
            return
        
        City.objects.all().delete()
        Tour.objects.all().delete()
        Booking.objects.all().delete()

        for _ in range(int(options['count'] * 0.5)):
            
            city = City()
            city.locale = random.choices(locales)[0]
            fake = Faker(city.locale)
            city.name = fake.city()
            city.country = fake.current_country()
            city.save()
            self.stdout.write(self.style.SUCCESS('Successfully added %s!' % city.name))

        self.stdout.write(self.style.NOTICE('------------------------------------------------------'))

        for _ in range(int(options['count'] * 0.3)):
            city_from, city_to = random.sample(list(City.objects.all()), 2)
            fake = Faker(city_from.locale)
            tour = Tour()
            tour.title = fake.sentence(nb_words=8)
            tour.desc = fake.paragraph(nb_sentences=5)
            tour.from_city = city_from
            tour.to_city = city_to
            tour.from_date = fake.date_between('today', '+1w')
            tour.to_date = fake.date_between('+2w', '+4w')
            td : timedelta = tour.to_date - tour.from_date
            tour.price = randrange(100,210) * td.days
            tour.save()
            self.stdout.write(self.style.SUCCESS('Successfully added tour from %s to %s!' % (tour.from_city, tour.to_city)))

        self.stdout.write(self.style.NOTICE('------------------------------------------------------'))

        for _ in range(int(options['count'] * 0.2)):
            booking = Booking()
            booking.client = User.objects.order_by('?').first()
            booking.tour = Tour.objects.order_by('?').first()
            booking.book_date = timezone.now()
            booking.status = 'pending'
            booking.save()
            self.stdout.write(self.style.SUCCESS('%s successfully booked a tour from %s to %s!' % (booking.client.first_name, booking.tour.from_city, booking.tour.to_city)))

        self.stdout.write(self.style.NOTICE('------------------------------------------------------'))
        
        self.stdout.write(self.style.SUCCESS('Successfully filled database!'))
