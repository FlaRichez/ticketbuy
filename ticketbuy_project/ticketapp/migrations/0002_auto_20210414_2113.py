# Generated by Django 3.1 on 2021-04-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
