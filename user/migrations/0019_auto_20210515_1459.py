# Generated by Django 3.2 on 2021-05-15 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_channel_statistics_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel_statistics',
            name='category',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='channel_statistics',
            name='logo_low',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]