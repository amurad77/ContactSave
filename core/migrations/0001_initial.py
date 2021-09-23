# Generated by Django 3.2.7 on 2021-09-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last Name')),
                ('number', models.CharField(max_length=15, verbose_name='Number')),
                ('email', models.EmailField(max_length=40, verbose_name='E-mail')),
                ('password', models.CharField(max_length=10, verbose_name='Password')),
            ],
        ),
    ]