# Generated by Django 3.0.3 on 2020-09-21 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BbsApp', '0002_bbs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='regdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
