# Generated by Django 3.2.8 on 2021-12-02 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Force_HLG', '0014_alter_vectorslog_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='pretestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=25)),
                ('user', models.CharField(blank=True, max_length=25)),
                ('timeStamp', models.CharField(max_length=100)),
            ],
        ),
    ]
