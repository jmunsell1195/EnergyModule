# Generated by Django 3.2.8 on 2021-12-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Force_HLG', '0017_pretestlog2'),
    ]

    operations = [
        migrations.CreateModel(
            name='vectorsMouseEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('user', models.CharField(blank=True, max_length=25)),
                ('timeStamp', models.CharField(max_length=100)),
                ('mouseX', models.CharField(blank=True, max_length=25)),
                ('mouseY', models.CharField(blank=True, max_length=25)),
                ('clickX', models.CharField(blank=True, max_length=25)),
                ('clickY', models.CharField(blank=True, max_length=25)),
                ('clickedITMtl', models.CharField(blank=True, max_length=25)),
                ('clickedITMbr', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='vectors',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='vectors',
            name='feedbackTime',
        ),
        migrations.RemoveField(
            model_name='vectors',
            name='instructionTime',
        ),
        migrations.RemoveField(
            model_name='vectors',
            name='numClicks',
        ),
        migrations.RemoveField(
            model_name='vectors',
            name='quiz1Time',
        ),
        migrations.RemoveField(
            model_name='vectors',
            name='quiz2Time',
        ),
        migrations.RemoveField(
            model_name='vectorslog',
            name='videoNumber',
        ),
        migrations.RemoveField(
            model_name='vectorslog',
            name='videoTime',
        ),
        migrations.AddField(
            model_name='vectorslog',
            name='clickX',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='vectorslog',
            name='clickY',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
