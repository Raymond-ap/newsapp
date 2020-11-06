# Generated by Django 3.0.7 on 2020-10-08 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=40)),
                ('publisher_profile', models.FileField(blank=True, upload_to='pics')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('images', models.FileField(blank=True, upload_to='pics')),
                ('category', models.CharField(choices=[('Business', 'Business'), ('Sports', 'Sports'), ('Technology', 'Technology'), ('Entertainment', 'Entertainment'), ('Health', 'Health'), ('Life style', 'Life style'), ('Celebrities', 'Celebrities')], default=3, max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]