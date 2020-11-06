# Generated by Django 3.0.7 on 2020-10-08 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20201008_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='is_popular',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='celebrities',
            name='is_popular',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='entertainment',
            name='is_popular',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='health',
            name='is_popular',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='lifestyle',
            name='is_popular',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='sport',
            name='is_popular',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='technology',
            name='is_popular',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]