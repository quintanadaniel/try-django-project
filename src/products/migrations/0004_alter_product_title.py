# Generated by Django 3.2.8 on 2021-10-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_produtc_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
