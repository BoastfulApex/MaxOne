# Generated by Django 4.1.1 on 2022-10-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0008_product_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('count', models.IntegerField()),
            ],
        ),
    ]
