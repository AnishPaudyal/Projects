# Generated by Django 4.0.3 on 2022-04-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_sell_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='condition',
            field=models.CharField(choices=[('Used', 'Used'), ('New', 'New')], default='New', max_length=100, null=True),
        ),
    ]
