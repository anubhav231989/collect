from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.name

class Quote(models.Model):
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, blank=True)
    quotation = models.TextField()

    def __str__(self):
        return self.quotation


