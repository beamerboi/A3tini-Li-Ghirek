# Generated by Django 3.2 on 2021-07-16 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopotion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='phoneNumber',
        ),
    ]