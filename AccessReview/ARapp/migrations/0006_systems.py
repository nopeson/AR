# Generated by Django 5.0.1 on 2024-01-14 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARapp', '0005_users_manageremployeeid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Systems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systemName', models.CharField(max_length=255)),
                ('criticality', models.CharField(max_length=255)),
            ],
        ),
    ]
