# Generated by Django 2.2.19 on 2021-04-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('assignee', models.CharField(max_length=100)),
            ],
        ),
    ]
