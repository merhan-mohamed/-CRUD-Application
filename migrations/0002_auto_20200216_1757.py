# Generated by Django 2.2.6 on 2020-02-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project5', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]