# Generated by Django 4.1.7 on 2023-03-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media')),
                ('UTC', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'photo',
            },
        ),
    ]
