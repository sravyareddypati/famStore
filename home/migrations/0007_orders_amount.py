# Generated by Django 2.2.14 on 2022-07-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]