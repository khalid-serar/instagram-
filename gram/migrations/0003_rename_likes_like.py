# Generated by Django 3.2.9 on 2021-12-06 05:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gram', '0002_likes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='likes',
            new_name='Like',
        ),
    ]
