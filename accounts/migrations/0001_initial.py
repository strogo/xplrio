# Generated by Django 2.2.7 on 2019-11-26 06:50

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photography_type', models.CharField(default='', max_length=500, null=True)),
                ('risk_level', models.CharField(default='', max_length=500, null=True)),
                ('profile_pic', models.ImageField(default='', max_length=500, null=True, upload_to='')),
                ('recent_ip', models.GenericIPAddressField(default='27.0.0.0', null=True)),
            ],
            options={
                'db_table': 'UserProfile',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]