# Generated by Django 3.2.3 on 2021-06-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartementModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('descrip', models.TextField())
            ],
        ),
    ]
