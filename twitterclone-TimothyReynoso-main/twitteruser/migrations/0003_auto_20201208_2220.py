# Generated by Django 3.1.4 on 2020-12-08 22:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0002_myuser_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='followers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
