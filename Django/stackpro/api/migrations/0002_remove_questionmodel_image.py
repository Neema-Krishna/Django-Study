# Generated by Django 4.2.4 on 2023-09-30 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionmodel',
            name='image',
        ),
    ]