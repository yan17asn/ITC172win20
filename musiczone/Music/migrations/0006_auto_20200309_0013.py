# Generated by Django 3.0.2 on 2020-03-09 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0005_auto_20200308_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='length',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='track',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]