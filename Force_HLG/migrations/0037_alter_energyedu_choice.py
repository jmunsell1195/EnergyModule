# Generated by Django 4.1.1 on 2022-09-18 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Force_HLG', '0036_alter_energyedu_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energyedu',
            name='choice',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
