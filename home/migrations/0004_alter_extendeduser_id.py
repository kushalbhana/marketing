# Generated by Django 3.2 on 2021-05-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_extendeduser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
