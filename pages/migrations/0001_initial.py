# Generated by Django 3.0.7 on 2021-10-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('Designation', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('facebook', models.URLField(max_length=100)),
                ('google', models.URLField(max_length=100)),
                ('twitter', models.URLField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]