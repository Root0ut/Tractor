# Generated by Django 4.0.3 on 2023-08-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfextract', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='url',
            name='date',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='url',
            name='keyword',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='url',
            name='user_id',
            field=models.TextField(null=True),
        ),
    ]
