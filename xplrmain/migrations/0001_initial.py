# Generated by Django 2.2.7 on 2019-12-03 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGoPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.CharField(default='0, 0', max_length=500, null=True)),
                ('difficulty', models.CharField(default='Low', max_length=500, null=True)),
                ('description', models.CharField(default='', max_length=500, null=True)),
                ('time_to_go', models.CharField(default='Any Time', max_length=500, null=True)),
                ('verified', models.BooleanField(default=False, max_length=100, null=True)),
                ('go', models.ManyToManyField(to='xplrmain.UserGoPost')),
            ],
        ),
        migrations.CreateModel(
            name='UserVisitedPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xplrmain.UserPost')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserSavedPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xplrmain.UserPost')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='userpost',
            name='saved',
            field=models.ManyToManyField(to='xplrmain.UserSavedPost'),
        ),
        migrations.AddField(
            model_name='userpost',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userpost',
            name='visited',
            field=models.ManyToManyField(to='xplrmain.UserVisitedPost'),
        ),
        migrations.AddField(
            model_name='usergopost',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xplrmain.UserPost'),
        ),
        migrations.AddField(
            model_name='usergopost',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
        ),
    ]
