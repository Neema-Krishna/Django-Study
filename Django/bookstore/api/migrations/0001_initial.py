# Generated by Django 4.2.4 on 2023-08-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookstore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('Description', models.CharField(max_length=200)),
            ],
        ),
    ]
