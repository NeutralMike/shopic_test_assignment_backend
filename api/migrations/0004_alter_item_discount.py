# Generated by Django 3.2.7 on 2021-09-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_cart_status_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
