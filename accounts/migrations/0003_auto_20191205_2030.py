# Generated by Django 2.2.7 on 2019-12-05 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191204_0913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertouserfriendship',
            old_name='following',
            new_name='friend',
        ),
    ]
