# Generated by Django 3.2.2 on 2021-05-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicmodels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='result',
            field=models.TextField(blank=True),
        ),
    ]
