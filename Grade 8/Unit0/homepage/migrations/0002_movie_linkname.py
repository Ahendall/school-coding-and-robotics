# Generated by Django 4.0.1 on 2022-02-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='linkName',
            field=models.CharField(default='', max_length=200),
        ),
    ]