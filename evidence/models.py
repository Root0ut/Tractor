from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


# Create your models here.

class Evidence(models.Model):
    class Meta:
        db_table="evidence"
        verbose_name="증거"
    title=models.CharField(max_length=64, verbose_name="제목")
    content=models.CharField(max_length=256)
    created_at=models.DateTimeField(auto_now_add=True)
    attached=models.FileField('첨부 파일', upload_to='uploads/', null=True)
    file_name=models.CharField(max_length=256, null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    crime=models.CharField(max_length=200)



