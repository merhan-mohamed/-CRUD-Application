# Generated by Django 2.2.6 on 2020-02-17 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project5', '0002_auto_20200216_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project5.Author'),
        ),
    ]
