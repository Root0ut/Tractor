# Generated by Django 4.0.3 on 2023-08-17 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='ans5',
            field=models.TextField(null=True),
        ),
    ]