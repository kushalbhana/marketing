# Generated by Django 3.2 on 2021-05-18 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_extendeduser_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extendeduser',
            old_name='search_query',
            new_name='Min_amount',
        ),
    ]
