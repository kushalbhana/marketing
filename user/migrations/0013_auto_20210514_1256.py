# Generated by Django 3.2 on 2021-05-14 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0012_channel_statistics_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphAnalitycs',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('subsgoal', models.CharField(max_length=100)),
                ('subsgoal_current_position', models.CharField(max_length=50)),
                ('substoviewratio', models.TextField(max_length=10000)),
                ('views_to_like', models.CharField(max_length=50)),
                ('overall_rating', models.CharField(max_length=50)),
                ('total_comment', models.CharField(max_length=50)),
                ('overall_marking', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='mostpopularvideo',
        ),
    ]
