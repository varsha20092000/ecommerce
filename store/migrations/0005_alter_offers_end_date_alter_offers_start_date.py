# Generated by Django 4.1.4 on 2023-02-10 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_offers_end_date_alter_offers_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='offers',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
