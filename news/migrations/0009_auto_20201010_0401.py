# Generated by Django 3.0.7 on 2020-10-10 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20201008_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='publisher_profile',
        ),
        migrations.RemoveField(
            model_name='celebrities',
            name='publisher_profile',
        ),
        migrations.RemoveField(
            model_name='entertainment',
            name='publisher_profile',
        ),
        migrations.RemoveField(
            model_name='health',
            name='publisher_profile',
        ),
        migrations.RemoveField(
            model_name='lifestyle',
            name='publisher_profile',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='publisher_profile',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='publisher_profile',
        ),
    ]