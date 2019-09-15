from django.db import models
from django.utils import timezone

# Create your models here.
GENDER_CHOICES = (
    ("M","M"),
    ("F","F")
)

GENRE_CHOICES = (
    ("ACTION","ACTION"),
    ("DRAMA","DRAMA"),
    ("THRILLER","THRILLER"),
    ("ROMANCE","ROMANCE"),
    ("COMEDY","COMEDY"),
    ("HORROR","HORROR"),
    ("SCI-FI","SCI-FI"),
    ("DOCUMENTARY","DOCUMENTARY")
)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES,default="M")

    def __str__(self):
        return self.name

class Movie(models.Model):
    created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=60)
    genre = models.CharField(max_length=15,choices=GENRE_CHOICES)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Cast(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.PROTECT)
    cast = models.ForeignKey("Actor", on_delete=models.PROTECT)

    def __str__(self):
        return self.cast.name

