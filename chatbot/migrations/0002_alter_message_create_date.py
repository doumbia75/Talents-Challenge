# Generated by Django 4.2.5 on 2023-09-15 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 15, 18, 50, 8, 59731, tzinfo=datetime.timezone.utc)),
        ),
    ]
