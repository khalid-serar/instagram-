# Generated by Django 3.2.9 on 2021-12-05 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photolikes', to='gram.image')),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userlikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
