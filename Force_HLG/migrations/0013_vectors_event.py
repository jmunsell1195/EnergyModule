# Generated by Django 3.2.8 on 2021-11-26 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Force_HLG', '0012_auto_20211126_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='vectors',
            name='event',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
