# Generated by Django 3.0.8 on 2020-07-16 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_movie_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_url',
            field=models.CharField(max_length=99999),
        ),
    ]
