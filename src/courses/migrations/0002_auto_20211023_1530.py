# Generated by Django 3.2.8 on 2021-10-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
        migrations.AddField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=0),
        ),
    ]
