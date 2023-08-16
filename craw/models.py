from django.db import models

class CrawData(models.Model):
    link = models.URLField()
    user_id = models.TextField()
    date = models.TextField()
    comment = models.TextField()

# Create your models here.
