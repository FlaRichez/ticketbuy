# Generated by Django 3.1 on 2021-04-14 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketbuy_app', '0003_auto_20210414_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='area',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='userprofile',
        ),
        migrations.RemoveField(
            model_name='ticketplace',
            name='place',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='Places',
        ),
        migrations.DeleteModel(
            name='ticket',
        ),
        migrations.DeleteModel(
            name='TicketPlace',
        ),
    ]