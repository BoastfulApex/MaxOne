# Generated by Django 4.1.1 on 2022-09-22 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='color',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='color',
            name='image4',
        ),
    ]
