# Generated by Django 3.1.7 on 2021-03-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='cost',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='стоимость'),
        ),
    ]
