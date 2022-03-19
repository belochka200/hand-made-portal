# Generated by Django 4.0.3 on 2022-03-09 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(blank=True, upload_to='', verbose_name='User avatar')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('status', models.CharField(blank=True, default='', max_length=255, verbose_name='Status')),
                ('raiting', models.PositiveIntegerField(default=0, verbose_name='Rainting')),
                ('is_salesman', models.BooleanField(default=False, verbose_name='Is Salesman')),
                ('verification', models.BooleanField(default=False, verbose_name='Verification')),
                ('shop_background', models.CharField(default='#FFFFFF', max_length=255, verbose_name='Shop background')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
