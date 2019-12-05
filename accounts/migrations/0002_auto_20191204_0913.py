# Generated by Django 2.2.7 on 2019-12-04 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='', max_length=500, null=True, upload_to='media/profile_pics'),
        ),
        migrations.CreateModel(
            name='UserToUserFriendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_connected', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='friendship_creator', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='friend', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]