# Generated by Django 3.0.8 on 2020-07-17 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler_api', '0008_auto_20200717_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler_api.Department'),
        ),
        migrations.AlterField(
            model_name='course',
            name='creditHours',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler_api.Teacher'),
        ),
        migrations.AlterField(
            model_name='room',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler_api.Department'),
        ),
        migrations.AlterField(
            model_name='section',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler_api.Department'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='day',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler_api.Department'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='timing',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler_api.Department'),
        ),
    ]
