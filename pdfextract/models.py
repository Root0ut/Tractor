from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.URLField(max_length=300)
    create_date = models.DateTimeField(auto_now_add=True,null=True)
    pdfpath = models.CharField(max_length=300, null=True)
    dflag=models.BooleanField(default=False)
    user_id = models.TextField(null=True)
    date = models.TextField(null=True)
    comment = models.TextField(null=True)
    keyword = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.url
