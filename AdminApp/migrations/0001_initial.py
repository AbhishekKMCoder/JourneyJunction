# Generated by Django 5.1 on 2024-08-21 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Location', models.CharField(max_length=300)),
                ('Description', models.TextField()),
                ('Price', models.CharField(max_length=100)),
                ('Duration', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
    ]