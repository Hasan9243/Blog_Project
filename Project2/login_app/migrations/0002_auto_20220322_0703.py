# Generated by Django 3.0 on 2022-03-22 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='facebook_id',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Profile_Pics'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
