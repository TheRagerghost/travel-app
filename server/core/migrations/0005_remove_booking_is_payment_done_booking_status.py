# Generated by Django 4.0.5 on 2022-07-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_booking_client_alter_booking_tour_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_payment_done',
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='undefined', max_length=50, verbose_name='status'),
            preserve_default=False,
        ),
    ]
