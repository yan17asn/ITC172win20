# Generated by Django 3.0.2 on 2020-02-02 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Club', '0004_auto_20200202_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
