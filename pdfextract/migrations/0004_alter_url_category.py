# Generated by Django 4.0.3 on 2023-08-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfextract', '0003_url_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='category',
            field=models.CharField(choices=[('선택', None), ('모욕죄', '모욕죄'), ('명예훼손죄', '명예훼손죄'), ('음란죄', '음란죄')], default='선택', max_length=10),
        ),
    ]
