from django.utils import timezone
from random import randint
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

locales = ['en_US', 'de_DE', 'en_GB', 'fr_FR']
Faker.seed(randint(0, 999999))


class Command(BaseCommand):
    help = 'Adds random user'

    def add_arguments(self, parser) -> None:
        parser.add_argument('count', type=int, nargs='?', default=20)

    def handle(self, *args, **options):

        for _ in range(options['count']):
            fake = Faker(random.choices(locales)[0])
            data = fake.simple_profile()
            user = User.objects.create_user(username=data['username'], 
                                        email=data['mail'], 
                                        password='iamuser',
                                        first_name=data['name'], 
                                        last_name=data['sex'],
                                        date_joined=timezone.now(),
                                        last_login=timezone.now())

            self.stdout.write(self.style.SUCCESS('Successfully added %s to the database!' % user.first_name))
