from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    is_menu = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FlashNews(models.Model):
    title = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=70)
    small_briff = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)


class SliderRepeat(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=70)
    small_briff = models.CharField(max_length=200)
    image = models.ImageField(upload_to='reverse/')
    test = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class LatestNews(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='latest/')

    def __str__(self):
        return self.title
