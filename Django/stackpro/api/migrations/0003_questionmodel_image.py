# Generated by Django 4.2.4 on 2023-09-30 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_questionmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]