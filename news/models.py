from django.db import models
from datetime import datetime


categories = (
    ("Business", "Business"),
    ("Sports", "Sports"),
    ("Technology", "Technology"),
    ("Entertainment", "Entertainment"),
    ("Health", "Health"),
    ("Life style", "Life style"),
    ("Celebrities", "Celebrities"),
)


class Entertainment(models.Model):
    publisher = models.CharField(max_length=40)

    post_banner = models.FileField(upload_to="pics", blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.FileField(upload_to="pics", blank=True)
    category = models.CharField(
        max_length=50, choices=categories, default="Entertainment")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    is_popular = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title


class Sport(models.Model):
    publisher = models.CharField(max_length=40)
    post_banner = models.FileField(upload_to="pics", blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.FileField(upload_to="pics", blank=True)
    category = models.CharField(
        max_length=50, choices=categories, default="Sports")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    is_popular = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title


class Business(models.Model):
    publisher = models.CharField(max_length=40)
    post_banner = models.FileField(upload_to="pics", blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.FileField(upload_to="pics", blank=True)
    category = models.CharField(
        max_length=50, choices=categories, default="Business")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    is_popular = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title


class Technology(models.Model):
    publisher = models.CharField(max_length=40)
    post_banner = models.FileField(upload_to="pics", blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.FileField(upload_to="pics", blank=True)
    category = models.CharField(
        max_length=50, choices=categories, default="Technology")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    is_popular = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title


class Health(models.Model):
    publisher = models.CharField(max_length=40)
    post_banner = models.FileField(upload_to="pics", blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.FileField(upload_to="pics", blank=True)
    category = models.CharField(
        max_length=50, choices=categories, default="Health")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    is_popular = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title


class Celebrities(models.Model):
    publisher = models.CharField(max_length=40)
    post_banner = models.FileField(upload_to="pics", blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.FileField(upload_to="pics", blank=True)
    category = models.CharField(
        max_length=50, choices=categories, default="Celebrities")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    is_popular = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title


class LifeStyle(models.Model):
    publisher = models.CharField(max_length=40)
    post_banner = models.FileField(upload_to="pics", blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.FileField(upload_to="pics", blank=True)
    category = models.CharField(
        max_length=50, choices=categories, default="Life style")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    is_popular = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title


class BreakingNews(models.Model):
    publisher = models.CharField(max_length=40)
    post_banner = models.FileField(upload_to="pics")
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title
