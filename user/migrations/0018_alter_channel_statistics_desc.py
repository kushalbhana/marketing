# Generated by Django 3.2 on 2021-05-14 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_channel_statistics_overall_marking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel_statistics',
            name='desc',
            field=models.TextField(default='', max_length=9000),
        ),
    ]