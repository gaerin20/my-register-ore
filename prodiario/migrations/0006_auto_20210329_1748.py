# Generated by Django 2.2.17 on 2021-03-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodiario', '0005_auto_20210329_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diario',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]