# Generated by Django 4.2.3 on 2024-08-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('number', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
