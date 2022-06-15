# Generated by Django 4.0.5 on 2022-06-15 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_image', models.ImageField(upload_to='')),
                ('actor_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('zodic_sign', models.CharField(max_length=10)),
                ('drame_name', models.CharField(max_length=255)),
                ('actor_profile', models.TextField()),
                ('update_datetime', models.DateTimeField()),
            ],
        ),
    ]
