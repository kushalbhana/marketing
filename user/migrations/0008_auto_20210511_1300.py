# Generated by Django 3.2 on 2021-05-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210508_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel_statistics',
            name='id',
        ),
        migrations.RemoveField(
            model_name='mostpopularvideo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='id',
        ),
        migrations.AddField(
            model_name='channel_statistics',
            name='desc',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='channel_statistics',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mostpopularvideo',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
