# Generated by Django 3.0.8 on 2020-07-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler_api', '0013_auto_20200717_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='timing',
            field=models.CharField(max_length=15),
        ),
    ]