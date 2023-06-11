from django.db import models

# Create your models here.
class MediaFile(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    url = models.URLField(max_length=1000, verbose_name="URL")

    def __str__(self):
        return str(self.title)
