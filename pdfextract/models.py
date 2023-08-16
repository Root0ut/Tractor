from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.URLField(max_length=300)
    create_date = models.DateTimeField(auto_now_add=True,null=True)
    pdfpath = models.CharField(max_length=300, null=True)
    dflag=models.BooleanField(default=False)
    
    def __str__(self):
        return self.url
