# Generated by Django 4.2.1 on 2024-09-28 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharebite', '0008_coordinator_age_coordinator_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
