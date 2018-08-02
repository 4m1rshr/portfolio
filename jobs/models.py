from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField(max_length=250)

