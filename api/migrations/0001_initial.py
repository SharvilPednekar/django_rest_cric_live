# Generated by Django 3.2.8 on 2021-10-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('test_captain', models.CharField(max_length=100)),
                ('one_Day_captain', models.CharField(max_length=100)),
                ('first_Test', models.TextField()),
                ('first_Odi', models.TextField()),
                ('first_T20', models.TextField()),
                ('association', models.CharField(max_length=200)),
                ('coaches', models.TextField()),
            ],
        ),
    ]