# Generated by Django 3.2.8 on 2021-10-18 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_produtc_summary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produtc',
            new_name='Product',
        ),
    ]
