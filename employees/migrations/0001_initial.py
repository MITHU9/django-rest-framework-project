# Generated by Django 5.2 on 2025-04-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
    ]
