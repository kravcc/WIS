# Generated by Django 4.1.3 on 2022-11-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_termin_date_termin_max_points_termin_repeted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='termin',
            name='description',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
