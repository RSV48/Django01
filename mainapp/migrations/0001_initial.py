# Generated by Django 3.1.7 on 2021-03-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='наиментование категории')),
                ('description', models.TextField(blank=True, verbose_name='описание категории')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='дата создания категории')),
            ],
        ),
    ]
