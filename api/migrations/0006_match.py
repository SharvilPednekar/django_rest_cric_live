# Generated by Django 3.2.8 on 2021-10-18 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('result', models.CharField(blank=True, max_length=100, null=True)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.venue')),
            ],
        ),
    ]
