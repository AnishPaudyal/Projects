# Generated by Django 3.1.2 on 2022-04-22 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20220422_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
