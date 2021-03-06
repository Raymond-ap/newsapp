# Generated by Django 3.0.7 on 2020-10-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20201010_0401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breaking_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=40)),
                ('post_banner', models.FileField(upload_to='pics')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
