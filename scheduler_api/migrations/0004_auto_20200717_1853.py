# Generated by Django 3.0.8 on 2020-07-17 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler_api', '0003_auto_20200717_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='course',
            new_name='courses',
        ),
    ]
