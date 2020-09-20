# Generated by Django 3.0.8 on 2020-07-17 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler_api', '0012_auto_20200717_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler_api.Department')),
            ],
            options={
                'unique_together': {('name', 'department')},
            },
        ),
        migrations.AddField(
            model_name='class',
            name='timetable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scheduler_api.Timetable'),
        ),
    ]
